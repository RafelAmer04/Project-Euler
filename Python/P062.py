def ArePermutation(n,m):
    ns = list(str(n))
    ms = list(str(m))
    ns.sort()
    ms.sort()
    return ns == ms


def test_list_of_cubes(permutations,cubes):
    if len(cubes) == 0:
        return permutations
    if len(permutations) + len(cubes) < 3:
        return []
    if len(permutations) == 3:
        return permutations
    for i in range(len(cubes) - 1):
        if len(permutations) == 0:
            permutations.append(cubes[i])
        elif ArePermutation(permutations[-1],cubes[i]):
            permutations.append(cubes[i])
        cubes = cubes[i+1:]
        r = test_list_of_cubes(permutations, cubes)
        if len(r) == 3:
            return r
        if len(permutations) != 0:
            permutations.pop()
    return []

limit = 8

while limit < 9:
    k1 = int(10**(limit/3))

    if k1**3 < 10**limit:
        k1 += 1

    k2 = int((10**(limit+1)-1)**(1/3))
    l = [x**3 for x in range(k1, k2+1)]
    r = test_list_of_cubes([],l)
    if len(r) == 3:
        print (r)




    limit += 1












