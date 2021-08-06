from functions.functions import FactorInteger


def phi(n):
    f = FactorInteger(n)
    p = n
    for i in f:
        p *= 1 - 1/i[0]
    return p

min = 28748
sol = 0


for i in range(2, 10000000):
    p = phi(i)
    if len(str(p)) != len(str(i)):
        continue
    pr = [int(x) for x in str(p)]
    ir = [int(x) for x in str(i)]
    if len(set(ir+pr)) == len(ir) and i/p < min:
            min = i/p
            sol = i

print(sol)
