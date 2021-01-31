import math


def IsPentagonal(n):
    if n <= 0:
        return False
    n = (1 + math.sqrt(24 * n + 1)) / 6
    return((n - int(n)) == 0)
#
# j = 1
# D = 0
#
# while D == 0:
#     for k in range(1, j):
#         if IsPentagonal(j) and IsPentagonal(k):
#             print(j, " ", k)
#             s = j + k
#             d = j - k
#             if IsPentagonal(s) and IsPentagonal(d):
#                 D = abs(d)
#     j += 1
#
#
# print(D)

D = 0
PL = []
n = 1



while D == 0:
    PL.append(n*(3*n-1)//2)
    sum = PL[-1]
    for j in range(1, len(PL)):
        for k in range(1, j):
            PJ, PK = PL[j], PL[k]
            if PJ + PK == sum:
                # print(PK, " ", PJ, " ", sum)
                if IsPentagonal(PJ - PK):
                    D = abs(PJ - PK)
    n += 1

print(D)
