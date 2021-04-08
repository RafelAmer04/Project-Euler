total = 0
values = [200,100,50,20,10,5,2,1]

def count_options(actual,value):
	global total
	global values
	if value > 200:
		return
	if value == 200:
		total += 1
		return
	l = len(actual)
	if l == 8:
		return
	d = 200 - value
	m = d // values[l]
	for i in range(0,m+1):
		value += i*values[l]
		actual.append(i)
		count_options(actual,value)
		del actual[-1]
		value -= i*values[l]

count_options([],0)

print("The number of different ways can £2 be made using any number of coins is: " +  str(total))