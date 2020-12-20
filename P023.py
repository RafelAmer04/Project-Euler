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


#Calculate all abundant numbers below 28123

n = 28123
a = []
s = 0
b = []
x = 0
sol = 0

for i in range(12, n+1):
    if SumaDivisors(i) > i:
       a.append(i)

for i in range(len(a)-1):
    for j in range(i, len(a)-1):
        suma = a[i] + a[j]
        if suma <= n and suma not in b:
            s += suma
            b.append(suma)



print(s)

for i in range(n+1):
    x += i

sol = x - s

print(sol)




# for i in range(len(a)-1):
#     for j in range(i, len(a)-1):
#         suma = a[i] + a[j]
#         if suma not in s:
#             s = np.append(s, suma)
#
#
# for i in range(28123):
#     if i not in s:
#         sol += i
#
