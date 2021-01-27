c = ""
for i in range(200000):
    c += str(i)


sol = 1

for t in range(7):
    k = 10**t
    sol *= int(c[k])

print(sol)
