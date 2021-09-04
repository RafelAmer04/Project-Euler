total = 0
values = list(range(10, 0, -1))

def count_options(actual,value):
	global total
	global values
	if value > 10:
		return
	if value == 10:
		total += 1
		return
	l = len(actual)
	if l == 10:
		return
	d = 10 - value
	m = d // values[l]
	for i in range(0,m+1):
		value += i*values[l]
		actual.append(i)
		count_options(actual,value)
		del actual[-1]
		value -= i*values[l]

count_options([],0)

print(total)