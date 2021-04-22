def Score(t):
    n = map(ord, t)
    n = sum([x >= 65 and x <= 122 for x in n])
    return n / len(t)


f = open("P059.txt", "r")
t = f.read()
t = t.strip()
t = list(map(int, t.split(",")))
f.close()


A = "abcdefghijklmnopqrstuvwxyz"
P = 0

for n1 in A:
    for n2 in A:
        for n3 in A:
            n = [ord(n1),ord(n2),ord(n3)]
            text = []
            p = 0
            for l in t:
                text.append(chr(l ^ n[p % 3]))
                p += 1
            text = "".join(text)
            S = Score(text)
            if S > P:
                P = S
                T = text


T = sum(map(ord, T))

print(T)











    

