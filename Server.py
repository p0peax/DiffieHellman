from Bob import *
from ProgramConstants import g,p
from Crypto.PublicKey import RSA
from Crypto import Random
from ProgramConstants import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER
from twilio.rest import TwilioRestClient


def setupk(request, db):
    global b, key
    username = request.form['username']
    password = request.form['password']
    phone_number = request.form['phone_number']

    db.insert({
        'username': username,
        'password': password,
        'phone_number': phone_number
    })

    b = Bob(p,g,int(password))
    print(password)
    key = RSA.generate(1024, Random.new().read)
    pk = key.publickey()
    f = open('static/publickey.pub','w+')
    f.write(pk.exportKey().decode())
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    #message = client.messages.create(body=str(b.beta),to=phone_number,from_="+13437000753")


def login1(m1):
    global b
    if b.validatem1(m1) :
        print ("Key Validated From Alice")
    m = b.compute_k()
    print(int.from_bytes(m,"big"),key.sign(m,''))
    return



