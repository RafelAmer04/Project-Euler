sol = 0
for a in range(1, 999):
    for b in range(1, 999):
        for c in range(1, 999):
            if a + b + c == 1000 and (a**2) + (b**2) == (c**2):
               sol = (a*b*c)
               print(sol)
