sum = 1
s = 2

for i in range(1, 501):
    max = (2*i+1)**2
    sum += 4*max-6*s
    s += 2

print(sum)
