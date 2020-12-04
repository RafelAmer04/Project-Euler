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

j = 1
p = 0
while p < 10001:
    j += 1
    if prime(j):
        p += 1


print(j)