sol = 0
for a in range(1, 999):
    for b in range(1, a+1):
        c = 1000 - a - b
        if (a**2) + (b**2) == (c**2):
            sol = (a*b*c)

print(sol)
