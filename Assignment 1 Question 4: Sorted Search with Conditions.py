'''
Given a list of random values between 0 and 1 and a random value x:
• Sort the list.
• Find all indices where the list value is greater than or equal to x.
• Print the sorted list, the value of x, and the first matching index (if one exists).
'''

from random import random

values = [random() for i in range(20)]
x = random()

values.sort()       # sorts the list
matching_index = []       # find all indices where value is greater than or equal to x
for i in range(len(values)):
    if values[i] >= x:
        matching_index.append(i)

print("sorted list:", values)
print("x:", x)
if len(matching_index) > 0:         # printing first matching index
    print("first matching index:", matching_index[0])
else:
    print("none")