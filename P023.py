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
def DivisorSum(n):
    s = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            s += i
    return s



#Calculate all abundant numbers below 28123

a = []
s = []
sol = 0

for i in range(12, 28124):
    if DivisorSum(i) > i:
        a.append(i)


for i in range(len(a)-1):
    for j in range(i, len(a)-1):
        suma = a[i] + a[j]
        if suma not in s:
            s.append(suma)


for i in range(28124):
    if i not in s:
        sol += i

print(sol)






