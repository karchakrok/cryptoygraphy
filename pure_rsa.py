# Implémentation purement mathématique du RSA.
from arithmetic import modular_inverse, euclid
from random import randint


def generate_key(p,q):
    n = p * q
    phin = (p - 1) * (q - 1)
    e = randint(1,phin)

    while euclid(e,phin) != 1:
        e = randint(1,phin)

    d = modular_inverse(e, phin)
    return p,q,n,phin,d,e

def encipher(m,n,e):
    return pow(m, e, n)

def decipher(c,n,d):
    return pow(c, d, n)

"""
print("****** generate_key ******")
p,q,n,phin,d,e=  generate_key(31,73)
print("pq == n : ", p*q==n)
print("(p-1)*(q-1) == phi(n) : ", (p-1)*(q-1) == phin)
print("1 <= e < phi(n): ",e>0 and e<phin)
print("1 <= d < phi(n): ",d>0 and d<phin)
print("PGCD(e,phin)==1: ", euclid(e,phin) == 1)
print("ed =1 mod phin", (e*d) % phin  == 1)
print("****** cipher and decipher ******")
m= randint(1,n-1)
c = encipher(m,n,e)
print("chiffrement de ",m,":", c)
print("d�chiffrement de ",c,":", decipher(c,n,d)
"""