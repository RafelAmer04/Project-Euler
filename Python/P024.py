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


# NextLexi([1,2,3,4,5,6,7,8,9,10,11,12,13])
# print(NextLexi([5,3,6,4,1,10,2,13,12,11,9,8,7]))
# NextLexi([13,12,11,10,9,8,7,6,5,4,3,2,1])


# n = [1,2,3,4,5,6]
# times = 0
#
#
# while n:
#     print(n)
#     n = NextLexi(n)
#     times +=1
#
# print(times)

n = [0,1,2,3,4,5,6,7,8,9]
times = 1

while times < 1000000:
    n = NextLexi(n)
    times +=1



n = "".join(map(str,n))
print(n)