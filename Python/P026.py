

def length_recurring_cycle(n):
	r = 1
	remainders = []
	while True:
		r = r % n
		if r == 0:
			return 0
		if r in remainders:
			i = remainders.index(r)
			return len(remainders) - i
		else:
			remainders.append(r)
		r *= 10

max = 0
sol = 0
for i in range(1,1000):
	l = length_recurring_cycle(i)
	if l > max:
		max = l
		sol = i
		
print(sol)