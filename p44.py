#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import math
import sys

def is_pentagonal(x):
    t = (1.0+math.sqrt(1.0+24.0*x))/6.0
    if t.is_integer():
        return True
    return False

def pentagonal(n):
    return n*(3*n-1)/2

n = 1
while True:
    p = pentagonal(n)
    m = 1
    while m < n:
        q = pentagonal(m)
        if is_pentagonal(p-q) and is_pentagonal(p+q):
            print(p, q, p-q, p+q)
            sys.exit(0)
        m += 1
    n += 1
