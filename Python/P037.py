import math

def prime(p):
    p = int(p)
    q = math.sqrt(p)
    if p == 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    i = 3
    while i <= q:
        if p % i == 0:
            return False
        i += 2
    return True

def IsTruncable(p):
    temp = str(p)
    for i in range(len(str(p))):
        if not prime(temp):
            return False
        temp = temp[:-1]

    temp = str(p)

    for i in range(len(str(p))):
        if not prime(temp):
            return False
        temp = temp[1:]
    return True


count, i = 0, 12
sum = 0

while count != 11:
    if IsTruncable(i):
        print(i)
        count += 1
        sum += i
    i += 1

print(sum)
