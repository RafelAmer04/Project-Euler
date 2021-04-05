import math


def IsPrime(p):
    p = int(p)
    q = math.sqrt(p)
    if p == 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    i = 3
    while i <= q:
        if p % i == 0:
            return False
        i += 2
    return True


def NextPrime(n):
    if n % 2 == 0:
        n += 1
    else:
        n += 2
    while not IsPrime(n):
        n += 2
    return n 


def FactorInteger(n):
    f = []
    e = 0
    
    while n % 2 == 0:
        n //= 2
        e += 1
    if e > 0:
        f.append((2, e))

    j = 3

    while n != 1:
        e = 0
        if IsPrime(n):
            f.append((n,1))
            return f
        while n % j == 0:
            n //= j
            e += 1
        if e > 0:
            f.append((j, e))
        j += 2                    
    return f