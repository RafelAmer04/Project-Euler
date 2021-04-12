from functions.functions import *

PL = []
SPL = [0]


for i in range(1, 1000001):
    if IsPrime(i):
        PL.append(i)
        SPL.append(SPL[-1] + i)
    

l = 0
sol = 0

for p in range(len(PL)):
    for n in range(p+1, len(PL)):
        s = SPL[p] - SPL[n]
        if s in PL and n-p > l:
            l = n-p
            sol = s

print(sol)