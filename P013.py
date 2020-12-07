f = open("P013.txt", "r")
t = str(f.read())
f.close()

t = t.replace("\n"," ")
t = t.split(" ")

list = []

for i in t:
    list.append(int(i))

sol = str(sum(list))[ : 10]
print(sol)
