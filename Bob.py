from DiffieHellman import *
import random

class Bob(DiffieHellman):

    alpha = 0

    def __init__(self, p_new, g_new, alpha):
        DiffieHellman.__init__(self, p_new, g_new)
        self.alpha = alpha
        self.beta = self.generate_random_b()

    def generate_random_b(self):
        self.b = random.randint(0, 100)
        self.beta = self.exponent_modulo(self.g,self.b, self.p)
        print("CELLPHONE MESSAGE + " + str(self.beta))
        return self.beta

    def compute_k(self):
        K = self.exponent_modulo(self.alpha, self.b, self.p)
        m = (str(self.beta) + str(self.alpha)).encode()
        return self.compute_m(m,K)

    def validatem1(self, m1):
        k_temp = self.exponent_modulo(self.alpha, self.b, self.p)
        m_temp = (str(self.alpha) + str(self.beta)).encode()
        m = int.from_bytes(self.compute_m(m_temp, k_temp), "big")
        print("m = " +str(m))
        print("m1 = " + str(m1))
        if m == int(m1):
            return True
        return False

