sol = 0
a = 0
b = 0


for i in range(1, 101):
    a += i**2
    b += i

sol = (b**2)-a
print(sol)