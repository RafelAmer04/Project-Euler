from functions.functions import IsPrime

total = 0
primes = []

def count_options(actual,value,count):
    global total
    global primes
    if len(primes) == 0:
        primes = [2]
    if number > primes[-1]:
        for i in range(primes[-1]+1,number+1):
            if IsPrime(i):
                primes.append(i)
    if value > number:
        return
    if value == number:
        total += 1
        return
    if len(actual) == 0:
        actual = [0 for p in primes]

    for i in range(count,len(primes)):
        if value + primes[i] > number:
            break
        actual[i] += 1
        value += primes[i]
        count_options(actual, value,count)
        actual[i] -= 1
        value -= primes[i]
        count += 1

ways = 0
number = 9
while(ways <= 5000):
    number += 1
    total = 0
    count_options([],0,0)
    ways = total

print(number)
print(primes)
