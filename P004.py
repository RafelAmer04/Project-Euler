m = 0

for a in range(100, 1000):
    for b in range(100, 1000):
        n = a * b
        string = str(n)
        rev = string[::-1]
        if string == rev and n > m:
            m = n

print(m)
