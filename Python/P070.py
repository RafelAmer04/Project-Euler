from functions.functions import FactorInteger

def phi(n):
    f = FactorInteger(n)
    p = n
    for i in f:
        p *= 1 - 1/i[0]
    return round(p)

def ArePermutation(n,m):
    ns = list(str(n))
    ms = list(str(m))
    ns.sort()
    ms.sort()
    return ns == ms


m = 10**8
sol = 0


for i in range(2, 10000001):
    p = phi(i)
    if not ArePermutation(i, p):
        continue

    if i/p < m:
        m = i/p
        sol = i


print(sol)
