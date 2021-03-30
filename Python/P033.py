from math import gcd

pd, pn = 1, 1


for d in range(10, 100):
    for n in range(10, d):
        ld = list(str(d))
        ln = list(str(n))
        for i in ln:
            if i == '0':
                continue
            if i in ld:
                ld.pop(ld.index(i))
                ln.pop(ln.index(i))
        if len(ln) == 1:
           ## print(ln,  ld)
            n1, d1 = int(ln[0]), int(ld[0]) 
            if d1 != 0 and n / d == n1 / d1:
                pd *= d1
                pn *= n1
sol = pd // gcd(pd, pn)

print(sol)

        