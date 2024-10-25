# Code 1
# An example tuple
name = ('Joe', 'Edward', 'Bloggs')
forename, middle, lastname = name
print(forename)

# Code 2
# Using the tuple() function
name = ['Joe', 'Edward', 'Bloggs']
tuple(name)

# Code 3
# Slicing a list
count = [0, 1, 2, 3, 4, 5]
count[0:2]

# Code 4
# Reversing a list
print(count[::-1])
count.reverse()
print(count)

# Code 5
# Using zip() for iteration
names = ['Bob', 'Fred', 'James', 'Neal']
ages = [20, 24, 27, 19]
salaries = ['30,000', '40,000', '35,000']

for name, age, salary in zip(names, ages, salaries):
    print(name, "is", age, "and has a salary of", salary, "pounds")

# Code 6
# An example list comprehension
comprehension = [number for number in range(1, 6) if number % 2 == 1]
comprehension