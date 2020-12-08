def func(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

def chain(n):
    d = 1
    while n > 1:
        n = func(n)
        d +=1
    return d

m = 0
n = 0

for i in range(1, 1000000):
    c = chain(i)
    if c > m:
        m = c
        n = i

print(n)

