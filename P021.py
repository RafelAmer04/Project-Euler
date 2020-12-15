def Divisors(n):
    s = 1
    if n % 2 == 0:
        for i in range(2, n//2+1):
            if n % i == 0:
                s += i
    else:
        for i in range(3, n//2+1, 2):
            if n % i == 0:
                s += i
    return s

sol = 0

for i in range(1, 10000):
    for j in range(i+1, 10000):
        if Divisors(i) == j and Divisors(j) == i:
            sol += i + j

print(sol)