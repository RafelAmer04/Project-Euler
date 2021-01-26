import math

def prime(p):
    q = math.sqrt(p)
    if p ==2:
        return True
    if p % 2 == 0:
        return False
    i = 3
    while i <= q:
        if p % i == 0:
            return False
        i += 2
    return True


class Rotations:
    def __init__(self, num):
        self.num = str(num)
        self.times = len(self.num)
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        if self.count <= self.times:
            t, num = num[-1], num[:-1]
            num = t + num
            self.num = num
            self.count += 1
            return self.num
        else:
            raise StopIteration

s = set()

for i in range(2, 1000000):
    if i in s:
        continue
    all = True
    t = set()
    for j in Rotations(i):
        j = int(j)
        if not prime(j):
            all = False
            break
        t |= {j}
    if all:
        s |= t

print(len(s), s)
