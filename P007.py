def prime(p):
    if p % 2 == 0:
        return False
    for i in range(3, p, 2):
            if p % i == 0:
                return False
    return True

j = 1
p = 0
while p < 10001:
    j += 1
    if prime(j):
        p += 1


print(j)