l = []

for i in range(100):
    for j in range(100, 10000):
        s = set(str(i)) | set(str(j))
        if "0" in s:
            continue
        if len(s) < 5:
            continue
        m = i*j
        s = s | set(str(m))
        if len(s) < 9 or "0" in s or len(str(m)) > 4:
            continue
        print(s,i,j,m)
        if m not in l:
            l.append(m)
sol = sum(l)

print(sol)




