'''
Define a function that receives a list of numbers and returns a dictionary where:
• Each key is a unique value from the list.
• Each value is the percentage of elements in the list that are less than or equal to that key.
The resulting dictionary should be sorted by key before being returned.
'''

def distributionAnalysis(list_of_numbers):
    result = {}
    total_count_of_numbers = len(list_of_numbers)
    unique_numbers = sorted(set(list_of_numbers))       # getting unique values from the list, no duplicates
    for value in unique_numbers:           # looping through each unique value
        count = 0
        for num in list_of_numbers:     # count how many numbers are less than or equal to the key
            if num <= value:
                count += 1
        percentage_of_elements = (count / total_count_of_numbers) * 100       # percentage

        result[value] = percentage_of_elements      # now store in dictionary

    return result

list_of_numbers = [3, 1, 2, 3, 4, 2]
print(distributionAnalysis(list_of_numbers))        # output