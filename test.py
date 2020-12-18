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
    s = 1
    f = Factor(n)
    for k,v in f.items():
        s *= (k**(v+1)-1)//(k-1)
    return s-n

def DivisorSum(n):
    s = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            s += i
    return s


n = 1509880500

print(SumaDivisors(n))

