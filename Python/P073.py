from math import gcd


sol = 0

for d in range(2, 1000001):
    if d % 100000 == 0:
        print(d)
    k1 = int(d / 3) + 1
    k2 = int(d / 2)
    for n in range(k1, k2+1):
        if gcd(n, d) == 1:
            sol += 1

print(sol)
