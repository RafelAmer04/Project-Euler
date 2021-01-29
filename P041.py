from functions.functions import IsPrime

from itertools import permutations

t = "123456789"
perm = [''.join(p) for p in permutations(t)]



lar = 0

for n in range(10):
    for i in perm:
        if IsPrime(i) and int(i) > lar:
            lar = int(i)
    if lar != 0:
        break
    t = t[:-1]
    perm = [''.join(p) for p in permutations(t)]

print(lar)
