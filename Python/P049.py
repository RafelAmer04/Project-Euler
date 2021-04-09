from functions.functions import *

sol = ""
primes = []

for i in range(1001, 10000, 2):
    if IsPrime(i):
        primes.append(i)

SP = {}
added = []

for p in primes:
    if p not in added:   
        SP[p] = [p]
    s1 = list(str(p))
    s1.sort()
    for q in primes:
        if q <= p:
            continue
        if q in added:
            continue
        s2 = list(str(q))
        s2.sort()
        if s1 == s2:
            SP[p].append(q)
            if q not in added:
                added.append(q)


for k,v in SP.items():
    if len(v) >= 3:
        for n1 in range(len(v)):
            for n2 in range(n1+1, len(v)):
                for n3 in range(n2+1,len(v)):
                    if v[n2] - v[n1] == v[n3] - v[n2]:
                        sol = str(v[n1]) + str(v[n2]) + str(v[n3])
                        print(sol)


