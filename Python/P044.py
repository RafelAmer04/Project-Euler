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


# import sys
#
# def is_pentagonal(x):
#     t = (1.0+math.sqrt(1.0+24.0*x))/6.0
#     if t.is_integer():
#         return True
#     return False
#
# def pentagonal(n):
#     return n*(3*n-1)/2
#
# n = 1
# while True:
#     p = pentagonal(n)
#     m = 1
#     while m < n:
#         q = pentagonal(m)
#         if is_pentagonal(p-q) and is_pentagonal(p+q):
#             print(p, q, p-q, p+q)
#             sys.exit(0)
#         m += 1
#     n += 1
