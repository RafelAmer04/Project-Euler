#!/usr/bin/python3

def ArePermutation(n,m):
    ns = list(str(n))
    ms = list(str(m))
    ns.sort()
    ms.sort()
    return ns == ms

done = False

def test_list_of_cubes(permutations,cubes):
    # print(permutations,cubes)
    global done
    if len(permutations) + len(cubes) < 5:
        return
    if len(permutations) == 5:
        print (permutations)
        done = True
        return
    for i in range(len(cubes) - 1):
        call = False
        if len(permutations) == 0:
            permutations.append(cubes[i])
            call = True
        elif ArePermutation(permutations[-1],cubes[i]):
            permutations.append(cubes[i])
            call = True
        if call :
            test = list(cubes[i+1:])
            test_list_of_cubes(permutations, test)
            if len(permutations) != 0:
                permutations.pop()
        if done:
            break

limit = 8

while True:
    m = limit - 1
    k1 = int(10**(m/3))

    if k1**3 < 10**m:
        k1 += 1

    k2 = int((10**(m+1)-1)**(1/3))
    l = [x**3 for x in range(k1, k2+1)]
    test_list_of_cubes([],l)
    if done:
        break
    limit += 1
