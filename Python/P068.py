from itertools import permutations

N = range(1,11)
lines = ((0,5,6),(1,6,7),(2,7,8),(3,8,9),(4,9,5))
sol = 0

for p in permutations(N):
    t = [[p[k] for k in l] for l in lines]
    if len(set(map(sum,t))) > 1:
        continue

    n = p[0:5]
    mi = n.index(min(n))
    y = []
    for l in range(mi, mi + 5):
        y += t[l%5]
    value = "".join(map(str,y))
    if len(value) > 16:
        continue
    value = int(value)
    if value > sol:
        sol = value

print(sol)
