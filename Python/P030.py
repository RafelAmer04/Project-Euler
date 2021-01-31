lim = 354294
sol = 0

for i in range(2, lim):
    k = str(i)
    s = 0
    for j in k:
        s += int(j)**5
    if s == i:
        sol +=  s


print(sol)

