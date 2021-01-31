f = open("P008.txt","r")
t = str(f.read())
f.close()
t = t.replace("\n","")

sol = 0

for i in range(987):
    p = 1
    for j in range(13):
        p *= int(t[i+j])
    if p > sol:
        sol = p

print(sol)