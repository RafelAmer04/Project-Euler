def divisors(n):
    e = []
    t = 2
    p = 1
    while n > 1:
        d = 0
        while n % t == 0:
            n = n//t
            d += 1
        if d != 0:
            e.append(d)
        if t == 2:
            t += 1
        else:
            t += 2
    for i in e:
        p *= i+1
    return p


t = 1
i = 2

while True:
    if divisors(t) >= 500:
        break
    t, i = t+i, i+1


print(t)





