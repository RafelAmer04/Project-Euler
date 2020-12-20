import math

def isPrime(p):
    if p <= 1:
        return False
    q = math.sqrt(p)
    if p % 2 == 0:
        return False
    i = 3
    while i <= q:
        if p % i == 0:
            return False
        i += 2
    return True

sol = 1
maxN = 0

for a in range(-999, 1000):
    for b in range(-999, 1001):
        n = 0
        while isPrime(n**2+a*n+b):
            n += 1
        if n-1 > maxN:
            maxN = n-1
            sol = a*b

print(sol)