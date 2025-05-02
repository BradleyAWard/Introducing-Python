# Code 1
# Define a function with arguments
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu(dessert = 'flan', entree = 'fish', wine = 'bordeaux')

# Code 2
# A function using *args
def print_args(required1, required2, *args):
    print('This argument is required: ', required1)
    print('This argument is required: ', required2)
    print('These arguments are optional: ', args)
    
print_args('Item1', 'Item2', 'Item3', 'Item4', 'Item5')

# Code 3
# Function using **kwargs
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
    
print_kwargs(wine = 'merlot', entree = 'mutton', dessert = 'macaroon')

# Code 4
# An example function
def cubic(x):
    '''
    This function cubes its input
    input: x
    output: x**3
    '''
    return x**3
help(cubic)

# Print just the docstring
cubic.__doc__

# Code 5
# Function to add any number of numbers
def sum_args(*args):
    return sum(args)

# Define a function that has a functional input
def run_with_positional_args(func, *args):
    return func(*args)

# Example use of this function
run_with_positional_args(sum_args, 1, 2, 3)

# Code 6
# An example generator function
def create_range(first = 0, last = 10, step = 1):
    number = first
    while number < last:
        yield number
        number += step
print(create_range())

# Using the generator function
for x in create_range():
    print(x)

# Code 7
# Our decorator function
def document(func):
    def new_function(*args, **kwargs):
        print("Running function: ", func.__name__)
        print("Positional arguments: ", args)
        print("Keyword arguments: ", kwargs)
        result = func(*args, **kwargs)
        print("Result: ", result)
        return result
    return new_function

# Decorating a function
@document
def addition(a, b):
    return a + b

# Running the decorated function
addition(3, 4)