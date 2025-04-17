# Code 1
# An example dictionary
dictionary = {'A': 1,
              'B': 2,
              'C': 3}

# Code 2
# Using the get() function
dictionary.get('D', 'Not in the dictionary')

# Code 3
# Using the keys() method
print(dictionary.keys())

# Using the values() method
print(dictionary.values())

# Using the items() method
print(dictionary.items())

# Code 4
# Combining dictionaries
dict1 = {'A': 1,
         'B': 2,
         'C': 3}

dict2 = {'D': 4,
         'E': 5,
         'F': 6}

dict3 = {'G': 7,
         'H': 8,
         'I': 9}

combined_dict = {**dict1, **dict2, **dict3}
combined_dict

# Code 5
# Iterating over keys
for key in dict1:
    print(key)

# Iterating over values
for value in dict1.values():
    print(value)

# Iterating over items
for item in dict1.items():
    print(item)