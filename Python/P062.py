def isCube(n):
    return round(n**(1.0/3))**3 == n

def NextLexi(n):
    i = 2
    l = len(n)
    while n[-i] > n[-i+1]:
        i += 1
        if i == len(n)+1:
            return None
    ant = n[0:l-i]
    piv = n[-i]
    post = n[l-i+1:]
    aux = [x for x in post if x > piv]
    m = min(aux)
    post.remove(m)
    post.append(piv)
    post.sort()
    r = ant + [m] + post
    return r

n = 2180
sol = 0

while sol == 0:
    n +=1
    cube = n**3
    scube = str(cube)
    perm = list(range(len(scube)))
    cubes = set()
    while perm is not None:
        t = int("".join([scube[i] for i in perm]))
        if isCube(t) and len(scube) == len(str(t)):
            cubes.add(t)
        perm = NextLexi(perm)
    if len(cubes) == 5:
        sol = cubes


print(sol)
print(n)








