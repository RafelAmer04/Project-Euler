f = open("P013.txt", "r")
t = str(f.read())
f.close()

t = t.replace("\n"," ")
t = t.split(" ")

t = list(map(int, t))


sol = str(sum(t))[ : 10]

print(sol)
