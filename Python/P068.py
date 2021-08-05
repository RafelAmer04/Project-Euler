from itertools import permutations

##N = range(1,11)
##lines = ((0,5,6),(1,6,5),(2,7,8),(3,8,9),(4,9,5))
N = range(1,7)
lines = ((0,3,4),(1,4,5),(2,5,3))
VALID = []

for p in permutations(N):
    t = [[p[l[k]] for k in l] for l in lines]
    t = set(map(sum(t)))

    if len(t) > 1:
        continue

    n = p[0:3]
    mi = n.index(min(n))
    y = []

    for l in range(mi, mi + 4):
        y += t[l%3]

print(VALID)





