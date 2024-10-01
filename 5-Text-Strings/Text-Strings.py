# Code 1
# Using a negative step count
name = "Joe Bloggs"
name[::-1]

# Code 2
# Using the split() and join() functions
string_numbers = '1, 2, 3, 4, 5'
list_numbers = string_numbers.split(',')
print(list_numbers)

string_numbers = ','.join(list_numbers)
print(string_numbers)

# Code 3
# String manipulation functions
name = "My name is Joe Bloggs"

print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase())

# Code 4
# String formatting with {} and .format()
name = "Joe Bloggs"
age = "30"

"My name is {} and I am {} years old".format(name, age)

# Code 5
# String formatting by position and name
"My name is {0} and I am {1} years old".format(name, age)
"My name is {name} and I am {age} years old".format(name=name, age=age)

# Code 6
# Using an f-string
f"My name is {name} and I am {age} years old"