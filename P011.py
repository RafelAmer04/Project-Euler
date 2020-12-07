m = []

with open ("P011.txt", "r") as f:
    for line in  f:
        line = line.rstrip()
        l = list(map(int, line.split(" ")))
        m.append(l)
f.close()

sol = 0
for x in range(17):
    for y in range(17):
        p = m[x][y] * m[x][y+1] * m[x][y+2] * m[x][y+3]
        if p > sol:
            sol = p
        p = m[x][y] * m[x+1][y+1] * m[x+2][y+2] * m[x+3][y+3]
        if p > sol:
            sol = p
        p = m[x][y] * m[x+1][y] * m[x+2][y] * m[x+3][y]
        if p > sol:
            sol = p

for x in range(16, 20):
    for y in range(17):
        p = m[x][y] * m[x][y+1] * m[x][y+2] * m[x][y+3]
        if p > sol:
            sol = p
        p = m[y][x] * m[y+1][x] * m[y+2][x] * m[y+3][x]
        if p > sol:
            sol = p

for x in range(19, 3, -1):
   for y in range(17):
     p = m[x][y] * m[x-1][y+1] * m[x-2][y+2] * m[x-3][y+3]
     if p > sol:
        sol = p

print(sol)
