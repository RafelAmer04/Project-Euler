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


i = 1
sol = 1

while True:
    if prime(i):
        if i >= 2000000:
            break
        else:
            sol += i
    i += 1

print(sol)

