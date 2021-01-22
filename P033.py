import math

f = [math.factorial(i) for i in range(10)]

def IsCurious(n):
    s = 0
    for i in str(n):
        #s += math.factorial(int(i))
        s += f[int(i)]
    if s == n:
        return True
    return False


s = 0
for i in range(3, 10000000):
    if IsCurious(i):
        s += i

print(s)
