import timeit

start = timeit.default_timer()

def Divisors(n):
    s = 1
    if n % 2 == 0:
        for i in range(2, n//2+1):
            if n % i == 0:
                s += i
    else:
        for i in range(3, n//2+1, 2):
            if n % i == 0:
                s += i
    return s

print(Divisors(10000))

stop = timeit.default_timer()

print('Time: ', stop - start)