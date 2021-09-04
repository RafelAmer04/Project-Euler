from math import sqrt
from math import gcd

def Triplet(m, n):
    if gcd(m,n) != 1:
        return None

    if m % 2 == 0 or n % 2 == 0:
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        return sum([a,b,c])

    return None


maxM = int(2000)+1

SumList = {}
sol = 0


for m in range(2, maxM):
    for n in range(1, m):
        T = Triplet(m, n)

        if T is None:
            continue

        k = 2

        while T <= 1500000:

            try:
                SumList[T]
            except:
                SumList[T] = 0
            SumList[T] += 1

            T *= k
            k += 1


for k,v in SumList.items():
    if k >= 1500000:
        continue
    if v == 1:
        sol += 1


print(sol)






