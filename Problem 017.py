# -*- coding: utf-8 -*-
"""
@author: NathanLHall
"""

# https://projecteuler.net/problem=17

one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7
thousand = 8
And = 3

# These are used to test the print out of the numbers as strings, to make sure
# all numbers are present
#ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',\
#        'eighteen', 'nineteen']
#tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#hundreds = ['hundred', 'And']

ones = [one, two, three, four, five, six, seven, eight, nine]
teens = [ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,\
        eighteen, nineteen]
tens = [twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety]
hundreds = [hundred, And]

total = 0

for i in range(0,9):
    total += ones[i]

for i in range(0,10):
    total += teens[i]

for i in range(0,8):
    total += tens[i]

for i in range(0,8):
    for j in range(0,9):
        total += tens[i] + ones[j]

for i in range(0,9):
    total += ones[i] + hundred

for i in range(0,9):
    for j in range(0,9):
        total += ones[i] + hundred + And + ones[j]

for i in range(0,9):
    for j in range(0,10):
        total += ones[i] + hundred + And + teens[j]

for i in range(0,9):
    for j in range(0,8):
        total += ones[i] + hundred + And + tens[j]

# Hundreds
for i in range(0,9):
    # Tens
    for j in range(0,8):
        # Ones
        for k in range(0,9):
            total += ones[i] + hundred + And + tens[j] + ones[k]

total += one + thousand
print(total)
