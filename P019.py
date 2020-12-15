#!/usr/bin/python3
# -*- coding: utf-8

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
    if f1[0] == f2[0] and f1[1] == f2[1] and f1[2] == f2[2]:
        return 0
    t = 0
    #
    # Anys sencers entre les dues dates
    #
    for y in range(f1[2]+1, f2[2]):
        t += NDaysYear(y)
    #
    # No esten el matreix any
    #
    if f2[2] > f1[2]:
        #
        # Mesos sencers des de la primera data fins a finals d'any
        #
        for m in range (f1[1] + 1,13):
            t += NDaysMonth(m,f1[2])
        #
        # Mesos sencers des de principis d'any fins a la segona data
        #
        for m in range (1,f2[1]):
            t += NDaysMonth(m,f2[2])
        #
        # Dies de l'últim mes
        #
        t += f2[0]
        #
        # Dies del primer mes
        #
        t += NDaysMonth(f1[1],f1[2]) - f1[0]
        return t
    #
    # Estem al mateix any
    #     Mesos sencers entre les dues dates
    #
    for m in range(f1[1] + 1,f2[1]):
        t += NDaysMonth(m,f1[2])
    #
    # Dies de l'últim mes
    #
    t += f2[0]
    #
    # Dies del primer mes
    #
    t += NDaysMonth(f1[1],f1[2]) - f1[0]
    return t

# d1 = (1,1,1900)
# sol = 0
#
#
# for y in range(1901, 7000):
#     for m in range(1, 13):
#         if CountDaysFrom(d1, (1,m,y)) % 7 == 6:
#             sol += 1



sol = 0
d = 0
for y in range(1901,7000):
    d += CountDaysFrom((1,1,y-1),(1,1,y))
    d = d % 7
    for m in range(1, 13):
        s = CountDaysFrom((1,1,y), (1,m,y))
        if (1 + d + s) % 7 == 0:
            sol += 1

print (sol)
