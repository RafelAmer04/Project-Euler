from sympy import *

def ContinousFraction(e):
    p = e[0] + Rational(1, e[1]+Rational(1, e[2] + Rational(1,e[3])))
    return p

    
e = [2]

for i in range(1, 2):
    e.append(1)
    e.append(2*i)
    e.append(1)


print(ContinousFraction(e))