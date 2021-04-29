#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

import networkx as nx
from functions.functions import IsPrime

primes = [2]
G = nx.Graph()

for k in range(3,10001):
    if IsPrime(k):
        primes.append(k)

for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        s1 = str(primes[i])
        s2 = str(primes[j])
        if IsPrime(int(s1+s2)) and IsPrime(int(s2+s1)):
            G.add_edge(primes[i],primes[j])

cliques = nx.find_cliques(G)
for c in cliques:
    if len(c) >= 5:
        print(c)
        print(sum(c))
