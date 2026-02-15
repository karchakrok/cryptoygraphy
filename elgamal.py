from random import randint

def generate_key_EG(g,p,q):
    r = randint(1,p-1)
    B = pow(g,r,p)
    return p,q,g,B,r

def encipher_EG(m,p,q,g,B):
    r = randint(1,p-1)
    c1 = pow(g,r,p)
    c2 = m * pow(B,r,p)
    return (c1,c2)

def decipher_EG(c,p,q,g,B,r):
    d1 = pow(c[0],-1,p) 
    d2 = c[1] * pow(d1,r,p) % p
    return d2 # d2 = m

if __name__ == "__main__":
    print("****** generate_key_EG ******")
    p,q,g,B,r=  generate_key_EG(5,73,72)
    print("B== g^r mod p : ", B==(g**r) % p)
    print(" 1 <= r < q : ", r>0 and r< q)
    print("****** cipher and decipher ******")
    p,q,g,B,r=  generate_key_EG(5,73,72)
    m=12
    c = encipher_EG(m,p,q,g,B)
    print("chiffrement de ",m,":", c)
    print("déchiffrement de ",c,":", decipher_EG(c,p,q,g,B,r))