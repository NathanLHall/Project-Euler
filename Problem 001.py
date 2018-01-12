# -*- coding: utf-8 -*-
"""
@author: NathanLHall
"""

# https://projecteuler.net/problem=1

subset = []

for i in range(3, 1000):
    if i % 3 == 0 or i % 5 ==0:
        subset.append(i)

print(sum(subset))
