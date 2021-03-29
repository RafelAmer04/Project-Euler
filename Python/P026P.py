#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Python 2!!!
#



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
value = 0
for i in xrange(1,1000):
	l = length_recurring_cycle(i)
	if l > max:
		max = l
		value = i

print "The value of d < 1000 for which 1/d contains the longest recurring cycle is: %d" % value