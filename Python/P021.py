def Divisors(n):
    s = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            s += i
    return s

sol = 0
d = {}
for i in range(1, 10001):
    d[i] = Divisors(i)




for i in range(1, 10000):
    for j in range(i+1, 10000):
        if d[i] == j and d[j] == i:
            sol += i + j

print(sol)