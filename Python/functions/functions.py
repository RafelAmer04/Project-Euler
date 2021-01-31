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
