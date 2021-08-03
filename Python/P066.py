from math import sqrt

def IsSquare(n):
    s = sqrt(n)
    return s == int(s)

maxX = 0
sol = 0 


for D in range(1001):
    if IsSquare(D):
        continue

    x = 1

    while True:
        x += 1
        t = x**2-1
        if t % D == 0 and IsSquare(t/D):
            if x > maxX:
                maxX = x
                sol = D
            break

print(sol)

