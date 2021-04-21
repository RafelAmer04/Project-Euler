from functions.functions import *

def Diagonals(n):
    if n == 0:
        return 1
    t = (2*n+1)**2
    return t, t-2*n, t-4*n, t-6*n

def NPrimes(n):
    return sum(map(IsPrime, Diagonals(n)))
    

Primes = 0
i = 0
per = 1

while per >= 0.1:
    i += 1
    Primes += NPrimes(i)
    per = Primes / (4*i + 1)
  

print(2*i+1)
