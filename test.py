#!/usr/bin/env python3

import itertools
 
values = [1, 2, 3, 4]
shells = []
 
com = itertools.combinations(values, 2)

i = 0
for val in com:
    shells.append([0, 0, 0, 0])
    for j in val :
        shells[i][j - 1] = 1
    i += 1

print("All possible combinations are", shells)