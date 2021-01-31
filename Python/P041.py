from functions.functions import IsPrime

from itertools import permutations

t = "123456789"
lar = 0



while len(t) > 1:
    for p in permutations(t):
        s = "".join(p)
        if IsPrime(s) and int(s) > lar:
            lar = int(s)
    if lar != 0:
        break
    t = t[:-1]

print(lar)
