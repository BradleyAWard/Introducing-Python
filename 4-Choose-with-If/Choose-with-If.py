# Code 1
# Boolean if statement
disaster = True

if disaster:
    print("Disaster!")
else:
    print("Calm")

# Code 2
# If statement with multiple options
colour = "yellow"

if colour == "red":
    print("The vegetable is red")
elif colour == "green":
    print("The vegetable is green")
elif colour == "yellow":
    print("The vegetable is yellow")
else:
    print("This probably isn't a vegetable")

# Code 3
# Using in for multiple comparisons
vowels = 'aeiou'
letter = 'o'
letter in vowels

# Code 4
# Using in for a dictionary
vowel_dict = {'a': 'alpha', 'e': 'echo', 'i': 'india', 'o': 'oscar', 'u': 'uniform'}
letter = 'o'
letter in vowel_dict

# Code 5
# Using the walrus operator
temperature_1 = 30
temperature_2 = 50

if diff := abs(temperature_2 - temperature_1) >= 10:
    print("The two temperatures are very different.")
else:
    print("The two temperatures are close enough.")