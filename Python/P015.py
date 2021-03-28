
def binomial(n, k):
    m = max(k,n-k)
    a = 1

    for i in range(m+1, n+1):
        a *= i
        a //= i-m

    return a


print(binomial(40, 20))
    