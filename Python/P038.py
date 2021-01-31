i = 1
l  = 0

while len(str(i) + str(i*2)) < 10:
    s = ""
    for j in range(1, 10):
        s = s + str(i*j)
        if len(set(s)) != 9 or "0" in set(s) or len(s) > 9:
            continue
        if int(s) > l:
            l = int(s)
    i += 1

print(l)
