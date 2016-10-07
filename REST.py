from Server import *
from Crypto.PublicKey import RSA
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
key = RSA.generate(1024)
db = TinyDB('static/database.db')


alpha, beta = 0, 0



@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def setup():
    setupk(request, db)
    return redirect(url_for('login'))


@app.route('/login', methods=['POST'])
def login():
    login1(request.form['username'])
    return redirect(url_for('login'))


@app.route('/login')
def login_template():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
