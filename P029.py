sol = 0
l = []

for a in range(2, 101):
    for b in range(2, 101):
        value = a**b
        if value not in l:
            l.append(value)

l.sort()

print(len(l))