def SumDigits(n):
    s = 0
    n = str(n)
    for d in n:
        s += int(d)

    return s

sol = 0

for a in range(1,100):
    for b in range(1, 100):
        t = SumDigits(a**b)
        if t > sol:
            sol = t

print(sol)
