from itertools import permutations

def SubDivisibility(n):
    div = [2,3,5,7,11,13,17]
    n = str(n)
    start = 1
    for div in div:
        check = ""
        for i in range(start, start+3):
            check = check + n[i]
        if int(check) % div != 0:
            return False
        start += 1
    return True


t = "0123456789"
sum = 0

for p in permutations(t):
    s = "".join(p)
    if SubDivisibility(s):
        sum += int(s)
print(sum)
