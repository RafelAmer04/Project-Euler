s = 2
a = 1
b = 2

while b <= 4000000:
   # i = a+b
   # a = b
   # b = i

   a,b = b,a+b

   if b % 2 == 0:
     s += b
print(s)