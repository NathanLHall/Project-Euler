# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:38:13 2018

@author: NathanLHall
"""

file = open("Problem 067.txt", 'r')
contents = file.readlines()
file.close()

temp = contents
contents = []

for line in temp:
    line = line.strip('\n')
    line = line.split(' ')
    for i in range(len(line)):
        line[i] = int(line[i])
    contents.append(line)

for i in range(len(contents) - 1):
    # The far left side has only one option to add to it from above
    contents[i+1][0] += contents[i][0]
    # The interior terms have two options
    for j in range(1, len(contents[i])):
        contents[i+1][j] += max(contents[i][j-1], contents[i][j])
    # The far right side has only one opttion to add to it from above
    contents[i+1][i+1] += contents[i][i]

print(max(contents[-1]))