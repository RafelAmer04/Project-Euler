def DivisorSum(n):
    s = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            s += i
    return s


#Calculate all abundant numbers below 28123

a =[]

for i in range(12, 28124):
    if DivisorSum(i) > i:
        a.append(i)


for i in range(1, 28123):
    for j in range(len(a)):
        if i
