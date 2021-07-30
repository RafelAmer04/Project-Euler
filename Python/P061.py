import sys


TRIANGULAR, SQUARE, PENTAGONAL, HEXAGONAL,  HEPTAGONAL, OCTAGONAL = [], [], [], [], [], []
TRI, SQU, PEN, HEX, HEP, OCT = 0, 0, 0, 0, 0, 0

POLIGONAL = {"TRIANGULAR": TRIANGULAR,
            "SQUARE":SQUARE,
            "PENTAGONAL": PENTAGONAL,
            "HEXAGONAL":HEXAGONAL,
            "HEPTAGONAL": HEPTAGONAL,
            "OCTAGONAL": OCTAGONAL}

n = 0
count = 0
 
while count < 6:
    n += 1

    if TRI == 0:
        l = n*(n+1)//2
        if l >= 10000:
            TRI = 1
            count += 1
        elif l >= 1000:
            TRIANGULAR.append(l)

    if SQU == 0:
        l = n**2
        if l >= 10000:
            SQU = 1
            count += 1
        elif l >= 1000:
            SQUARE.append(l)

    if PEN == 0:
        l = n*(3*n-1)//2
        if l >= 10000:
            PEN = 1
            count += 1
        elif l >= 1000:
            PENTAGONAL.append(l)

    if HEX == 0:
        l = n*(n-1)
        if l >= 10000:
            HEX = 1
            count += 1
        elif l >= 1000:
            HEXAGONAL.append(l)

    if HEP == 0:
        l = n*(5*n-1)//2
        if l >= 10000:
            HEP = 1
            count += 1
        elif l >= 1000:
            HEPTAGONAL.append(l)

    if OCT == 0:
        l = n*(3*n-2)
        if l >= 10000:
            OCT = 1
            count += 1
        elif l >= 1000:
            OCTAGONAL.append(l)


for i in range(10, 100):
    for j in range(10, 100):
        for k in range(10, 100):
            for l in range(10, 100):
                for m in range(10, 100):
                    for n in range(10, 100):

                        CC = {100*i+j,100*j+k,100*k+l,100*l+m,100*m+n, 100*n+i}
                        if len(CC) != 6:
                            continue
                        Q = set()
                        for x in CC:
                            for t,s in POLIGONAL.items():
                                if x in s:
                                    Q.add(t)
                        if len(Q) == 6:
                            print(CC)
                            sys.exit(0)
