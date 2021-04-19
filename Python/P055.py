
def IsPalindromic(n):
    n = str(n)
    return n == n[::-1]

def IsLychrel(n):
    for i in range(50):
        n = n + int(str(n)[::-1])
        if IsPalindromic(n):
            return 0
    return 1


sol = 0


for i in range(1, 10000):
    sol += IsLychrel(i)

print(sol)

