#!/usr/bin/env python3

import sys

locker_states = list(map(int, list(input("Please enter the current state of the lockers (for example 101010): "))))
num_num = int(input("Please enter the number of numbers: "))
numbers = input("Please enter the numbers seperated with a space: ").split()
len_numbers = len(numbers)
if(len_numbers != num_num) :
    print("Error: Number of numbers in the list is", len_numbers, "which doesn't match with", num_num )
    exit(1)
print("\nThe locker states are:", locker_states)
print(num_num, "numbers are entered and they are:", ', '.join(numbers))

# apply each number to all lockes
num_lockers = len(locker_states)
for num in numbers :
    print("\nApply number", num)
    for i in range(1, num_lockers + 1) :
        if(i % int(num) == 0) :
            locker_states[i - 1] = int(not bool(int(locker_states[i - 1])))
    print("The locker states are:", locker_states)

# count the number of locker that is in 0 state
count = 0
for state in locker_states :
    if state == 0 :
        count += 1
print("\nNumber of safe lockers is", count)
