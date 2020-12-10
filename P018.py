m = []

with open("P018.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        l = list(map(int, line.split(" ")))
        m.append(l)
f.close()

sol = m[0][0]
ly = 0

for i in range(1, 15):
    if m[i][ly] > m[i][ly+1]:
        sol += m[i][ly]
    else:
        sol += m[i][ly+1]
        ly = ly+1

print(sol)

