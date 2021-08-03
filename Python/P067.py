m = []

with open("P067.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        l = list(map(int, line.split(" ")))
        m.append(l)
f.close()


print(m)