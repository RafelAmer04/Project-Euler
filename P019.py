def IsLeap(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False


def NDaysYear(y):
    if IsLeap(y):
        return 366
    return 365


def NDaysMonth(m, y):
    if m in (1,3,5,7,8,10,12):
        return 31
    if m in (4,6,9,11):
        return 30
    if IsLeap(y):
        return 29
    return 28


def CountDaysFrom(f1, f2):
    t = 0
    for i in range(f1[2]+1, f2[2]):
        t += NDaysYear(i)
    t += NDaysMonth(f1[1], f1[2]) - f1[0]
    for i in range(f1[1]+1, 13):
        t += NDaysMonth(i, f1[2])
    t += f2[0]
    for i in range(1, f2[1]):
        t += NDaysMonth(i, f2[2])
    return t


d1 = (1,1,1900)
sol = 0
last = (1,1,1900)

for y in range(1901, 2001):
    for m in range(1, 13):
        if CountDaysFrom(d1, (1,m,y)) % 7 == 6:
            sol += 1
        last = (1,m,y)




print(sol)






