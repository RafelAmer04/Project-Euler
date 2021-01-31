def Factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def suma(n):
    s = 0
    n = str(n)
    for i in (n):
        s += int(i)
    return s

print(suma(Factorial(100)))
