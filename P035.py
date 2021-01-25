import math

def prime(p):
    q = math.sqrt(p)
    if p % 2 == 0:
        return False
    i = 3
    while i <= q:
        if p % i == 0:
            return False
        i += 2
    return True

def premutations:
    pass


lp = []

for i in range(1000000):
    if prime(i):
        lp.append(i)


for i in range(1000000):
    
