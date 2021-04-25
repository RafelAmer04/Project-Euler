TRIANGULAR, SQUARE, PENTAGONAL, HEXAGONAL,  HEPTAGONAL, OCTAGONAL = [], [], [], [], [], []
TRI, SQU, PEN, HEX, HEP, OCT = 0, 0, 0, 0, 0, 0 
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



print(PENTAGONAL)





print(len(TRIANGULAR),len(SQUARE), len(PENTAGONAL), len(HEXAGONAL), len(HEPTAGONAL),len(OCTAGONAL))