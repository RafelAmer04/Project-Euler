def to_letters(p):
    n = {
        1 : "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
    }
    if p == 1000:
        return "one "+ n[1000]
    if p <= 20:
        return n[p]
    if p < 100:
        u = p % 10
        d = p - u
        if u == 0:
            return n[d]
        return n[d] +"-"+ n[u]
    c = p // 100
    r = p - c * 100
    s = n[c] + " " + n[100]
    if r > 0:
        s += " and " + to_letters(r)
    return s


sol = 0

for i in range(1, 1001):
    l = to_letters(i)
    l = l.replace(" ", "")
    l = l.replace("-","")
    sol += len(l)

print(sol)



