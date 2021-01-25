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

def rotations(s):
    rot = [s]
    for i in range(len(s)-1):
        ls = []
        l = s[-1]
        s = s[:-1]
        s = l + s
        rot.append(s)
    return rot

print(rotations("197"))
