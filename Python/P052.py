sol = 0 
i = 1

while sol == 0:
    count = 0
    for m in range(2, 7):
        t = i*m
        if len(str(i)) == len(str(t)) and set(str(i)) == set(str(t)):
            count += 1
    if count == 5:
        sol = i
    i += 1

print(sol)