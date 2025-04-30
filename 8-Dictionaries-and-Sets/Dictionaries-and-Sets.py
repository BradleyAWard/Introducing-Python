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

# Code 6
# Example dictionary comprehension
vowels = 'aeiou'
word = 'onomatopoeia'

letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

vowel_counts = {letter: word.count(letter) for letter in word if letter in vowels}
print(vowel_counts)

# Code 7
# Defining a set
set('letters')

# Code 8
# Example dictionary with sets as values
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# Find keys in dictionary based on their set
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

# Code 9
# Find keys in dictionary based on combinations of set values
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

# Code 10
# Define two different sets
a = {1, 2, 3}
b = {2, 3, 4}

# In both A and B
a & b

# A or B
a|b

# In A but not in B
a - b

# In A or B but not both
a ^ b

# Code 11
# An example set comprehension
a_set = {number for number in range(1, 6)}
print(a_set)

# An example set with condition
b_set = {number for number in range(1, 6) if number % 3 == 1}
print(b_set)