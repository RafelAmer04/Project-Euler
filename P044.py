import math


def IsPentagonal( n ):
    if n <= 0:
        return False
    n = (1 + math.sqrt(24 * n + 1)) / 6
    return( (n - int (n)) == 0)

j = 1
D = 0

while D == 0:
    for k in range(1, j):
        if IsPentagonal(j) and IsPentagonal(k):
            print(j, " ", k)
            s = j + k
            d = j - k
            if IsPentagonal(s) and IsPentagonal(d):
                D = abs(d)
    j += 1


print(D)
