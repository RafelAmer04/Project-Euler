
def maxSum(m, f, c):
    s1 = m[f][c] + m[f+1][c]
    s2 = m[f][c] + m[f+1][c+1]
    return max(s1, s2)

m = []


with open("P067.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        l = list(map(int, line.split(" ")))
        m.append(l)
f.close()


for f in range(98, -1, -1):
    for c in range(0, f+1):
        m[f][c] = maxSum(m, f, c)


print(m[0][0])