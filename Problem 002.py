# -*- coding: utf-8 -*-
"""
@author: NathanLHall
"""

# https://projecteuler.net/problem=2

# Technically, the Fibonacci sequence starts with 1 and 1, not 1 and 2, but
# we can alter the definition to fit theirs.

Fib = [1, 2]
i = 0
subset = []

while Fib[-1] < 4000000:
    Fib.append(Fib[i] + Fib[i+1])
    i += 1

for i in range(len(Fib)):
    if Fib[i] < 4000000 and Fib[i] % 2 == 0:
        subset.append(Fib[i])

print(sum(subset))