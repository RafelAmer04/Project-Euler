a, b = 1, 1
i = 2


while b < 10**999:
    i += 1
    a, b = b, a+b


print(i)
