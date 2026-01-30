'''
Define a function that receives a list of strings and returns a dictionary with the following structure:

• Each key is a string from the list.

• Each value is another dictionary containing:
    – The length of the string
    – Whether the length is even or odd

'''

def nested_dictionary_from_strings(strings):
    dictionary = {}
    for s in strings:
        length = len(s)
        parity = "even" if length % 2 == 0 else "odd"

        dictionary[s] = {
            "length": length,
            "parity": parity
        }

    return dictionary

print(nested_dictionary_from_strings(["data","science"]))
