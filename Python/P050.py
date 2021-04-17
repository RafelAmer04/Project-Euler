from functions.functions import *

PL = [2]
SPL = [0,2]


for i in range(3, 1000001, 2):
    if IsPrime(i):
        PL.append(i)
        SPL.append(SPL[-1] + i)
    

l = 0
sol = 0

for p in range(len(SPL)):
    k = SPL[p]
    for n in range(p+1, len(SPL)):
        s = k - SPL[n]
        if s > 1000000:
            continue
        if s in PL and n-p > l:
            l = n-p
            sol = s

print(sol)