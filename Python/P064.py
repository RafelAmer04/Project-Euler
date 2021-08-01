from sympy import sqrt, simplify

def SqrtPeriod(n):
    PERIOD = 0
    REPETITION = []
    a = int(sqrt(n))
    b = sqrt(n) - a
    while True:
        a = int(1 / b)
        b = simplify(1 / b - a)
        if b in REPETITION:
            return PERIOD
        REPETITION.append(b)
        PERIOD += 1


sol = 0

SQUARES = [i**2 for i in range(101)]


for i in range(10001):
    if i in SQUARES:
        continue
    if SqrtPeriod(i) % 2 != 0:
        sol += 1

print(sol)
