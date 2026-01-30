'''
Define a function that computes x^y. Then, given a list of pairs (x, y):
• Use a for loop with argument unpacking to call the function.
• Skip any pair where the exponent y is negative.
• Store the valid results in a list and print the list.
'''

def safe_function_application(pairs):
    valid_results = []
    for x, y in pairs:
        if y < 0:       # skip the negative
            continue
        valid_results.append(x ** y)      # compute the x^y // storing valid results

    return valid_results

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]       # input list :D
print(safe_function_application(pairs))