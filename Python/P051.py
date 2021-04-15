from functions.functions import *

def Repetitions(n):
    r = {}
    s = str(n)
    for i in range(len(s)):
        k = int(s[i])
        try:
             r[k]
        except:
             r[k] = []
        r[k].append(i)
    r1 = {}
    for k in r.keys():
        if len(r[k]) > 1:
            r1[k] = r[k]
    return r1




sol = 0
PL = [0]

while sol == 0:
    PL.append(NextPrime(PL[-1]))
    P = PL[-1]
    r = Repetitions(PL[-1])

    if r == {}:
        continue


    r = Repetitions(P).values()
    l = list(map(int, str(P)))

    count = 0


    for i in r:
        for j in range(0, 10):
            for n in i:
                l[n] = j
           
            s = [str(h) for h in l]
            res = int("".join(s))
            
            if res not in PL or not IsPrime(res):
                continue
                count = 0
            
            count += 1
            l = list(map(int, str(P)))

    if count == 8:
        sol = P
    count = 0



print(sol)

    
    
    