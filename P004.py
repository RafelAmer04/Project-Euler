
for a in range(100, 999):
    for b in range(100, 999):
        string = str(a * b)
        rev = string[::-1]
        if string == rev:
            sol = string

print(sol)
