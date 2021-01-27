sol = 0
num = 0


for p in range(839, 841):
    t = 0
    for a in range(1, p-2):
        for b in range(1, a):
            c = p - (a+b)
            if a**2 == b**2 + c**2:
                t += 1
                print(a,b,c)
    if t > num:
        sol = p
        num = t

print(sol, num)

# num = {}
#
# for n in range(3, 1000):
#     if n % 2 == 0:
#         b = (n//2)**2 - 1
#         c = (n//2)**2 + 1
#     else:
#         b = n**2 // 2
#         c = b + 1
#
#     p = n + b + c
#     if p not in num:
#         num[p] = 0
#     num[p] += 1
#
#
# print(num)
