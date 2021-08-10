from fractions import *

closest = Fraction(2,5)
limit = Fraction(3,7)

for d in range(2, 1000001):
    k2 = int(3 * d / 7)
    f1 = Fraction(k2, d)
    if closest < f1 < limit:
        closest = f1

print(closest)




