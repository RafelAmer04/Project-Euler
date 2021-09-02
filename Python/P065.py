from sympy import *

def ContinousFraction(e):
    f = e[-1]
    for i in range(len(e)-2, -1, -1):
        f = e[i] + Rational(1,f)
    return f

    
e = [2]
sol = 0

for i in range(1, 105):
    e.append(1)
    e.append(2*i)
    e.append(1)


f = ContinousFraction(e[0:100])

s = str(f.p)

for j in s:
    sol += int(j)

print(sol)
