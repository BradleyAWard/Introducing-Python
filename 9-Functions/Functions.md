## 9) Functions

We do not wish to retype fragments of code all the time. The first step to code reuse is a function: a named piece of code that can take any number and type of input parameters and return any number and type of output results. You can define a function using zero or more parameters and call it to get zero or more results.

---

### Arguments and parameters

To avoid positional argument confusion, you can specify arguments by the names of their corresponding parameters, even in a different order from their definition in the function

```python
# Code 1
# Define a function with arguments
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu(dessert = 'flan', entree = 'fish', wine = 'bordeaux')
```

```output
{'wine': 'bordeaux', 'entree': 'fish', 'dessert': 'flan'}
```

We can also specify default values for parameters. The default is used if the caller does not provide a corresponding argument. When used inside the function with a parameter, an asterisk groups a variable number of positional arguments into a single tuple of parameter values. For example:

```python
# Code 2
# A function using *args
def print_args(required1, required2, *args):
    print('This argument is required: ', required1)
    print('This argument is required: ', required2)
    print('These arguments are optional: ', args)
    
print_args('Item1', 'Item2', 'Item3', 'Item4', 'Item5')
```

```output
This argument is required:  Item1
This argument is required:  Item2
These arguments are optional:  ('Item3', 'Item4', 'Item5')
```

Outside the function, `*args` explodes the tuple `args` into comma separated positional parameters. Inside the function, `*args` gathers all of the positional arguments into a single `args` tuple. You could use the names `*params` and `params`, but it is common practice to use `*args` for both the outside argument and inside parameter.

You can use two asterisks to group keyword arguments into a dictionary, where the argument names are the keys:

```python
# Code 3
# Function using **kwargs
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
    
print_kwargs(wine = 'merlot', entree = 'mutton', dessert = 'macaroon')
```

```output
Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
```

Inside the function, `kwargs` is a dictionary parameter. The argument order is: required positional arguments; optional positional arguments (`*args`); optional keyword arguments (`**kwargs`). As with `args`, you do not need to call this keyword arguments `kwargs`, but it is common usage.

---

### Docstrings

You can attach documentation to a function definition by including a string at the beginning of the function body. You can make a docstring long and even add rich formatting if desired. To print a docstring we call the `help()` function, or if you just want to see the raw docstring without formatting we can use the `.doc` internal variable.

```python
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
```

```output
Help on function cubic in module __main__:

cubic(x)
    This function cubes its input
    input: x
    output: x**3
```

```python
# Print just the docstring
cubic.__doc__
```

```output
'\n    This function cubes its input\n    input: x\n    output: x**3\n    '
```

---

### Functions are first-class citizens

In Python everything is an object. Functions are first-class citizens in Python; you can assign them to variables, use them as arguments to other functions and return them from functions. Let us consider an example by running a function with arguments. Here we define a test function that takes any number of positional arguments, calculates their sum using the `sum()` function and returns that sum. We can then define a new function `run_with_positional_args()` which takes a function and any number of positional arguments to pass to it.

```python
# Code 5
# Function to add any number of numbers
def sum_args(*args):
    return sum(args)

# Define a function that has a functional input
def run_with_positional_args(func, *args):
    return func(*args)

# Example use of this function
run_with_positional_args(sum_args, 1, 2, 3)
```

```output
6
```

---

### Generators

A generator is a Python sequence creation object. With it you can iterate through potentially huge sequences without creating and storing the entire sequence in memory at once. Every time you iterate through a generator, it keeps track of where it was the last time it was called and returns the next value. This is different to a normal function, which has no memory of previous calls and always starts at its first line with the same state.

If we want to create a large sequence we can write a generator function. It is like a normal function, but it return its value with a `yield` statement rather than `return`.

```python
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
```

```output
<generator object create_range at 0x10500d8c0>
0
1
2
3
4
5
6
7
8
9
```

A generator comprehension is surrounded by parentheses instead of square or curly brackets. It works as a shorthand version of a generator function, removing the `yield` command. It also return a generator object.

---

### Decorators

Sometimes we want to modify a function without changing its source code. A common example is adding a debugging statement to see what arguments were passed in. A decorator is a function that takes one function as input and returns another function. We shall show an example using `*args`, `**kwargs`, inner functions and functions as arguments. We shall define a function `document()` that will act as a decorator to print the function's name and the values of its arguments, run the function with the arguments, print the result and return the modified function for use. We shall use this to decorate a simple function that adds two numbers together.

```python
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
```

```output
Running function:  addition
Positional arguments:  (3, 4)
Keyword arguments:  {}
Result:  7
7
```

If we decorate a function with more than one decorator, we start with the one closest to the function (just above the definition) and then continue to the one above.

---

### Exceptions

When things go wrong, Python uses exceptions: code that is executed when an associated error occurs. When you run code that might fail under some circumstances, you also need appropriate exception handlers to intercept any potential errors. It is good practice to add exception handling anywhere an exception might occur to let the user know what is happening. If you do not provide your own exception handler, Python prints an error message and some information about where the error occurred and then terminates the program. We can use `try` to wrap our code and `except` to provide the error handling.
