import math

def IsPentagonal(n):
    if n <= 0:
        return False
    # NOTE: Check if sqrt(1 + 24n) is integer
    t = int(math.sqrt(1 + 24*n))
    if t**2 != 1 + 24*n:
        return False
    # NOTE: Check if t+1 is divisible by 6
    return (t+1) % 6 == 0

def IsHexagonal(n):
    if n <= 0:
        return False
    # NOTE: Check if sqrt(1 + 8n) is integer
    t = int(math.sqrt(1 + 8*n))
    if t**2 != 1 + 8*n:
        return False
    # NOTE: Check if t+1 is divisible by 4
    return (t+1) % 4 == 0


n = 3
s = 3
sol = 0

while sol == 0 or sol == 40755:
    if IsPentagonal(n) and IsHexagonal(n):
        sol = n
    print(n)
    n += s
    s += 1

print(sol)
    

    

