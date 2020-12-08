def sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    print(s)

p = 2**1000

sum(p)

