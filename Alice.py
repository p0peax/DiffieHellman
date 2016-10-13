from DiffieHellman import *
from Crypto.PublicKey import RSA
from ProgramConstants import g,p

class Alice(DiffieHellman):

    def __init__(self, p_new, g_new, password):
        DiffieHellman.__init__(self, p_new, g_new)
        self.a = password
        self.alpha = self.exponent_modulo(self.g, password, self.p)
        print("The password is " + str(self.alpha))

    def compute_k(self, text_message):
        self.beta = int(text_message)
        K = self.exponent_modulo(self.beta, self.a, self.p)
        m = str(str(self.alpha) + str(self.beta)).encode()
        return self.compute_m(m,K)

    def validatem2(self, m2):
        k_temp = self.exponent_modulo(self.beta, self.a, self.p)
        m_temp = (str(self.beta) + str(self.alpha)).encode()
        m = int.from_bytes(self.compute_m(m_temp, k_temp), "big")
        print("m = " + str(m))
        print("m1 = " + str(m2))
        if m == int(m2):
            return True
        return False



def main():
    password = input("Please enter a password")
    a = Alice(p, g, int(password))
    input("Click enter when the key is ready")
    f = open('static/publickey.pub')
    ik = f.read()
    pk = RSA.importKey(ik)
    text = input("Please enter the text message")

    #Generate Alice's m
    m1 = int.from_bytes(a.compute_k(text),"big")
    print(m1)

    #Receive m from server
    m2 = input("Please enter the server's m2")
    if a.validatem2(m2) :
        print("The keys are validated")
    else:
        print ("The keys are NOT validated")

    sig = input("Please enter the signature code")

    if pk.verify(int(m2), tuple([int(sig),''])):
        print("The signature has been verified")
    else:
        print ("The signature has not been validated")

if __name__ == "__main__":
    main()