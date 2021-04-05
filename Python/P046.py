from functions.functions import IsPrime
from functions.functions import NextPrime
import math

i = 9
PL = [2,3,5,7]
while True:
    
    NP = NextPrime(PL[-1])
    if NP < (i + 2):
        PL.append(NP)

    if IsPrime(i):
        i += 2
        continue

    g = False

    for p in PL:
        n = (i - p) // 2
        t = int(math.sqrt(n))
        if t**2 == n:
           g = True
           break
    
    if g == False:
        sol = i
        break
    
   

    i += 2


print(sol)