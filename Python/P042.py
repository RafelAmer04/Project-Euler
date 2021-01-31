import math

def IsTriangular(n):
    if n <= 0:
        return False
    # NOTE: Check if sqrt(1 + 8n) is integer
    t = int(math.sqrt(1 + 8*n))
    if t**2 != 1 + 8*n:
        return False
    # NOTE: Check if t is ODD
    return t % 2 != 0


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

f = open("P042.txt", "r")
t = f.read()
words = t.split(",")
f.close()

sol = 0

for w in words:
    w = w.replace('"', '')
    score = 0
    for l in w:
        score += d[l]
    if IsTriangular(score):
        sol += 1

print(sol)
