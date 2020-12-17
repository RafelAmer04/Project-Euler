def Factor(n):
    f = {}
    t = 2
    while n > 1:
        d = 0
        while n % t == 0:
            n = n//t
            d += 1
        if d != 0:
            f[t] = d
        if t == 2:
            t += 1
        else:
            t += 2
    return f

def SumaDivisors(n):
    s = 0
    f = Factor(n)


print(Factor(54))

