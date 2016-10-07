from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto import Random as rand
from ProgramConstants import g, p

class DHCrypto():

    a,b,g,p,K,alpha,beta = 0,0,0,0,0,0,0


    def __init__(self, p_new, g_new):
        self.p = p_new
        self.g = g_new


    def get_alpha(self, a):
        alpha = (self.g ** a) % self.p
        return alpha

    def generate_beta(self):
        self.b = rand.new().randint(0,100)
        self.beta = (self.g**self.b) % self.p
        return self.b

    @staticmethod
    def exponent_modulo(base, power, modulo):
        return (base ** power) % modulo

    @staticmethod
    def compute_m( m, K):
        k_bytes = K.to_bytes(32, "big")
        k2 = k_bytes[16:]
        mac = HMAC.new(k_bytes[:16])
        mac.update(m)
        aes = AES.new(k2, AES.MODE_CFB, b'\xe9\x8a]\xdc\xe5\xef\xb3\xc7x[t\xc6L\xea\x962')
        return_m = aes.encrypt(m + int(mac.hexdigest(), 16).to_bytes(32, "big"))
        return return_m





