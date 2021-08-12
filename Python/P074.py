from math import factorial

FACT = [factorial(x) for x in range(10)]

def SumDigitFactorial(n):
    s = 0
    for i in str(n):
        s += factorial(int(i))
    return s

sol = 0


for i in range(1, 1000000):
    if i % 10000 == 0:
        print(i)
    LF = [i]
    while True:
        Sum = SumDigitFactorial(LF[-1])
        if Sum in LF:
            if len(LF) == 60:
                sol += 1
            break
        LF.append(Sum)



print(sol)
