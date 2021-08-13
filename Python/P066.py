from sympy import *

def IsSquare(n):
    s = sqrt(n)
    return s == int(s)

def IsPellSolution(D,x,y):
    return x**2 - D*y**2 == 1

def ContinousFraction(e):
    f = e[-1]
    for i in range(len(e)-2, -1, -1):
        f = e[i] + Rational(1,f)
    return f

def FindPellSolution(n):
    REPETITION = []
    a = int(sqrt(n))
    b = sqrt(n) - a
    CONVERGENTS = [a]
    while True:
        a = int(1 / b)
        b = simplify(1 / b - a)
        f = ContinousFraction(CONVERGENTS)
        if isinstance(f,Rational) and IsPellSolution(n,f.p,f.q):
            return f.p,f.q
        CONVERGENTS.append(a)
        REPETITION.append(b)

maxX = 0
sol = 0

for D in range(2,1001):
    if IsSquare(D):
        continue

    x,y = FindPellSolution(D)
    if x > maxX:
        maxX = x
        sol = D

print(sol, maxX)
