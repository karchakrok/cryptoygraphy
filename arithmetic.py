def euclid(a:int, b:int) -> int:
    """
    Calcule le pgcd de a et b en utilisant l'algorithme d'Euclide.
    """
    a,b = abs(a),abs(b)
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def extended_euclid(a:int, b:int) -> tuple[int,int,int]:
    """
    Algorithme d'Euclide étendu. Retourne un triplet (d, u, v) tel que 
    au + bv = doù d = pgcd(a,b)
    """
    if b == 0:
        return abs(a), 1 if a > 0 else -1,0

    d, u1, v1 = extended_euclid(b, a % b)
    u = v1
    v = u1 - (a // b) * v1
    return d, u, v

def modular_inverse(a:int, n:int) -> int:
    """
    Calcule l'inverse de a modulo n.
    Retourne l'entier u tel que (a * u) % n == 1.
    Si l'inverse n'existe pas (d != 1), retourne 0.
    """
    n = abs(n)
    if n <= 1:
        raise ValueError("n doit être supérieur à 1.")
    
    d, u, v = extended_euclid(a % n, n) # a mod n
    if d != 1:
        raise ValueError(f"L'inverse de {a} mod {n} n'existe pas car non premiers entre eux.")
    else:
        return u % n

def naive_euler_function(n:int) -> int:
    """
    Calcule l'indicatrice d'Euler (phi) de manière naïve.
    Compte combien d'entiers entre 1 et n sont premiers avec n.
    """
    if n <= 1:
        return 0

    count = 0
    for i in range(1, n + 1):
        if euclid(i, n) == 1:
            count += 1
    return count

def euler_function(primes_list:list[int],exponents_list:list[int]) -> int:
    """
    Calcule l'indicatrice d'Euler d'un nombre à partir de sa 
    décomposition en facteurs premiers (primes_list^exponents_list).
    """
    n = 1
    if len(primes_list) != len(exponents_list):
        return 0
    
    for i in range(len(primes_list)):
        n *= primes_list[i] ** exponents_list[i]
    return naive_euler_function(n)

def inversible(n:int) -> list[int]:
    """
    Retourne la liste de tous les entiers inférieurs à n qui 
    possèdent un inverse modulaire (ceux qui sont premiers avec n).
    """
    if n < 0:
        raise ValueError("n doit être un entier positif.")
    
    return [i for i in range(n) if euclid(i,n) == 1]

def naive_exponentiation(base: int, exponent: int, modulo: int) -> int:
    """
    Calcule (base^exponent) % modulo par une méthode itérative simple.
    """
    if not (isinstance(base, int) and isinstance(exponent, int) and isinstance(modulo, int)):
        return "Saisir nb entiers"
    
    if exponent < 0:
        return "Saisir k positif"
    if exponent == 0:
        return 1 % modulo

    result = 1
    for _ in range(exponent):
        result = (result * base) % modulo
        
    return result

def square_and_multiply(base:int, exponent:int, modulo:int) -> int: # ~pow
    """
    Calcule (base^exponent) % modulo de manière optimisée en utilisant 
    l'exponentiation rapide (square and multiply).
    """
    result = 1
    exponent_binary = bin(exponent)[2:]
    
    for bit in exponent_binary:
        result = (result * result) % modulo  # square
        if bit == '1':
            result = (result * base) % modulo  # multiply
            
    return result