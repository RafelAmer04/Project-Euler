from functions.functions import FactorInteger


def phi(n):
    f = FactorInteger(n)
    p = n
    for i in f:
        p *= 1 - 1/i[0]
    return round(p)

sol = 0
max = 0

for i in range(2, 1000001):
    c = phi(i)
    if i/c > max:
        sol = i
        max = i/c


print(sol)
