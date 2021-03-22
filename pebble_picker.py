#!/usr/bin/env python3

import sys
import itertools

# list all possible shell locations
positions = [1, 2, 3, 4]
shells = []
com = itertools.combinations(positions, 2)

i = 0
for val in com:
    shells.append([0, 0, 0, 0])
    for j in val :
        shells[i][j - 1] = 1
    i += 1

print("All possible combinations are", shells)
""" shells = [\
[1, 1, 0, 0], \
[1, 0, 1, 0], \
[1, 0, 0, 1], \
[0, 1, 1, 0], \
[0, 1, 0, 1], \
[0, 0, 1, 1]] """

swap_guess = []
best_score = 0

num_swap = int(input("Input number of swaps: "))
for i in range(num_swap):
    swap_guess.append(list(map(int, list(input("Input swapped shells and guessed shells: ")))))

# print(num_swap)
# print(swap_guess)

# run through each possible shell locations
for p in range(len(shells)):
    score = 0
    print("Initial pebble locations are", shells[p])
    # run through each swap_guess try
    for t in range(num_swap):
        tmp = shells[p][swap_guess[t][0] - 1]
        shells[p][swap_guess[t][0] - 1] = shells[p][swap_guess[t][1] - 1]
        shells[p][swap_guess[t][1] - 1] = tmp
        print(shells[p])
        if shells[p][swap_guess[t][2] - 1] == 1 :
            score += 1
        if shells[p][swap_guess[t][3] - 1] == 1 :
            score += 1

    print("points scored in this combination is", score)
    if score > best_score : 
        best_score = score

print("The best score is", best_score)
