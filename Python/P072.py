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


sol = 0

for i in range(2, 1000001):
    sol += phi(i)

print(sol)