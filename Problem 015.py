# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:58:02 2018

@author: Omicron
"""
"""
Problem 15, if you draw it out, and treat it like a dynamic programming problem (i.e. start from
the finish point, and count paths back towards the start), you'll notice that it forms a
Pascal's triangle, if you follow the perimeter from bottom left, to top left, to top right.

If you follow the lattice from bottom to top, of the far right row, it'll be all ones.
If you follow the next row in, it'll be the naturals, which happen to be the sum of the
previous column entries, up to that height.
Again, the next row in is the triangular numbers, which are the sum of the naturals.
And on and on.  This pattern also works if you look across the rows, instead of columns.

So to find the top left value of an "m x n" lattice, where m = number of rows and n = number of 
columns, you'll want to find the nth column (so n loops through the summations) and pick the mth
entry in that column.
"""

set1 = [1] * 21
set2 = []

for count in range(1,21):
    for i in range(0,21):
        set2.append(sum(set1[0:i+1]))
    set1 = set2
    set2 = []

print(set1[20])