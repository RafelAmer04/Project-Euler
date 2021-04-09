sol = 0

for i in range(1, 1001):
    sol += i**i

print(sol%10**10)