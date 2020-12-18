import numpy as np

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

# def DivisorSum(n):
#     s = 1
#     for i in range(2, n//2+1):
#         if n % i == 0:
#             s += i
#     return s


#Calculate all abundant numbers below 28123
a = np.array([], np.int64)
s = np.array([], np.int64)
sol = 0

for i in range(12, 28124):
    if SumaDivisors(i) > i:
       a = np.append(a, i)

print(len(a))

for i in range(len(a)-1):
    for j in range(i, len(a)-1):
        suma = a[i] + a[j]
        if suma not in s:
            s = np.append(s, suma)


for i in range(28123):
    if i not in s:
        sol += i

print(len(s))
print(sol)
