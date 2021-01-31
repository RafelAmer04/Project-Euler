m = []

with open("P018.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        l = list(map(int, line.split(" ")))
        m.append(l)
f.close()

def suma(f, c, total):
    if f == total:
        return(m[f][c])
    a = suma(f+1, c, total)
    b = suma(f+1, c+1, total)

    if a > b:
        return m[f][c] + a
    return m[f][c] + b

sol = suma(0, 0, len(m)-1)

print(sol)