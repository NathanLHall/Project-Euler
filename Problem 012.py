# -*- coding: utf-8 -*-
"""
@author: NathanLHall
"""

# https://projecteuler.net/problem=12
import math
n = 1
triangular = 0
divisors = 0

while divisors < 501:
    triangular += n
    divisors = 0
    # The highest value to check for divisibility is the square root
    for m in range(1, math.floor(math.sqrt(triangular)) + 1):
        remainder = triangular % m
        if remainder == 0:
            # If the triangular number is a perfect square, only count the divisor once
            if m ** 2 == triangular:
                divisors += 1
            else:
                divisors += 2
    n += 1

print(triangular)
