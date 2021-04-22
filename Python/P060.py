from functions.functions import *
from itertools import combinations

def ConcatenatePrimes(l):
    if len(l) != 5:
        return False
    C = combinations(l, 2)
    for p in C:
        s1 = f"{p[0]}{p[1]}"
        s2 = f"{p[1]}{p[0]}"
        if not IsPrime(s1) or not IsPrime(s2):
            return False
    return True



PL = [2,3,5,7,11]


sol = 0


while sol == 0:
    C = combinations(PL, 4)
    for p in C:
        p = list(p) + [PL[-1]]
        if ConcatenatePrimes(p):
            sol = sum(p)
            sol2 = p
    PL.append(NextPrime(PL[-1]))


print(sol, sol2)