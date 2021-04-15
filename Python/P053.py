def binomial(n, k):
    m = max(k,n-k)
    a = 1

    for i in range(m+1, n+1):
        a *= i
        a //= i-m

    return a

sol = 0

for n in range(1, 101):
    for r in range(0, n+1):
        if binomial(n, r) > 1000000:
            sol += 1

print(sol)