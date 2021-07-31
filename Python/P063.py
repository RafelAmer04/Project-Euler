
sol = 0

for x in range(1, 10):
    n = 1 
    while len(str(x ** n)) == n:
        n += 1
        sol += 1

print(sol)