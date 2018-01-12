# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:48:31 2018

@author: Omicron
"""

power = 2 ** 1000
power = str(power)
digits = []

for i in range(len(power)):
    digits.append(power[i])

result = 0
for i in range(len(digits)):
    result += int(digits[i])

print(result)