'''
Write a Python program that multiplies consecutive integers starting from 1 until the product first
becomes greater than a given threshold value

Your program should:
• Store the threshold value in a variable.
• Keep track of the current multiplier.
• Print the final product and the integer that caused the product to exceed the threshold.

'''

threshold_value = 100
product = 1
currentNumber = 1

while product <= threshold_value:
    product *= currentNumber
    currentNumber += 1

print(product)  # output of exceeding threshold
print(currentNumber - 1)    # put output of integer that caused threshold


