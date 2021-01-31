sol = 0
num = 0


for p in range(1, 1000):
    t = 0
    for a in range(1, p-2):
        for b in range(1, a):
            c = p - (a+b)
            if a**2 == b**2 + c**2:
                t += 1
                print(a,b,c)
    if t > num:
        sol = p
        num = t

print(sol, num)
