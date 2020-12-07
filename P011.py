import numpy as np

f = open("P011.txt", "r")
t = str(f.read())
f.close()

t = t.replace("\n"," ")
list = t.split(" ")

arr = np.array(list)
arr = np.reshape(arr, (20, 20))

x, y = 0, 0
m = 1
sol = 0

for i in range(4):
    m *= int(arr[(x-i),y])
print(m)

print(arr[-2, 0])