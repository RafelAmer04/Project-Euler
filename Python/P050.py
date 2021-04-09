from functions.functions import *

PL = []

for i in range(1, 1000001):
    if IsPrime(i):
        PL.append(i)

l = 0
sol = 0

for p in range(len(PL)):
    for n in range(p+1, len(PL)):
        s = 0
        for i in range(p, n+1):
            s += PL[i]
        if s in PL and n-p > l:
            l = n-p
            sol = s

print(sol)