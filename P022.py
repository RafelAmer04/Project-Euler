def score(p, n):
    s = 0
    d = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    for i in range(len(p)):
        l = p[i]
        s += d[l]
    s *= n
    return s


f = open("P022.txt", "r")
t = f.read()
l = t.replace(']','').replace('[','')
l = l.replace('"','').split(",")

l.sort()

sol = 0

for i in range(len(l)):
    sol += score(l[i], i+1)
print(sol)
