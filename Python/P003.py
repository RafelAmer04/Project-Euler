num = 600851475143
d = 2

while num > 1:
    if num % d == 0:
        num = num//d
    else:
        d += 1
print(d)