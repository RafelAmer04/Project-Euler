import math

sol = 1
for i in range (1, 21):
    gcd = math.gcd(i, sol)
    sol *= i//gcd

print(sol)