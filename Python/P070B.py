from functions.functions import FirstFactor


def phi(n):
    F, E = FirstFactor(n)
    q = n / F**E

    if q == 1:
        P = F**(E-1) * (F-1)
        PhiList[n] = P
        return P

    P = PhiList[F**E] * PhiList[q]
    PhiList[n] = P
    return P

PhiList = {}


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
