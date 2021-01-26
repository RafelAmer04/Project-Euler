def Palindrome(s):
    s = str(s)
    return s == s[::-1]

def toBinary(n):
    bin = ""
    while n != 0:
        bin = str(n % 2) + bin
        n = n //2
    return bin

sol = 0

for i in range(1, 1000000):
    if Palindrome(i) and Palindrome(toBinary(i)):
        sol += i

print(sol)
