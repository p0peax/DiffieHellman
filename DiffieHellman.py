from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto import Random as rand

class DiffieHellman:

    __a,__b,__g,__p = 0,0,0,0
    __k,__alpha,__beta = 0,0,0

    def __init__(self, p_new, g_new):
        self.__p = p_new
        self.__g = g_new

    def get_alpha(self, a):
        self.__alpha = (self.__g ** a) % self.__p
        return self.__alpha

    def generate_beta(self):
        self.__b = rand.new().randint(0,100)
        self.__beta = (self.__g**self.__b) % self.__p
        return self.__b

    @staticmethod
    def exponent_modulo(base, power, modulo):
        return (base ** power) % modulo

    @staticmethod
    def compute_m(m, K):
        k_bytes = K.to_bytes(32, "big")
        k2 = k_bytes[16:]
        mac = HMAC.new(k_bytes[:16], SHA256.new())
        mac.update(m)
        aes = AES.new(k2, AES.MODE_CFB, b'\xe9\x8a]\xdc\xe5\xef\xb3\xc7x[t\xc6L\xea\x962')
        return_m = aes.encrypt(m + int(mac.hexdigest(), 16).to_bytes(32, "big"))
        return return_m





