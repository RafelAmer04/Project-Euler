total = 0
number = 100
values = list(range(number, 0, -1))

def count_options(actual, value):
    global total
    global values
    if value > number:
        return
    if value == number:
        total += 1
        return
    l = len(actual)
    if l == number:
        return
    d = number - value
    m = d // values[l]
    for i in range(0, m + 1):
        value += i * values[l]
        actual.append(i)
        count_options(actual, value)
        del actual[-1]
        value -= i * values[l]

count_options([], 0)

print(total - 1)
