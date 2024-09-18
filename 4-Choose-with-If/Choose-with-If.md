## 4) Choose with If

Many computer languages use characters or keywords to mark sections of code. In these languages it is good practice to use consistent indentation to make your code more readable for yourself and others. Python is unusual in that it uses white space to define program structure. Here we shall look at multiple-line commands.

---

### Compare with if, elif and else

Our first example is a Python program that checks the value of a boolean and prints an appropriate comment:

```python
# Code 1
# Boolean if statement
disaster = True

if disaster:
    print("Disaster!")
else:
    print("Calm")
```

```output
Disaster!
```

In this example we did the following: assigned a boolean value to the variable named *disaster*, performed a conditional comparison using `if` and `else`, executing different code depending on the value of *disaster* and calling the `print()` function to print some text. If there are more than two possibilities to test, use the `if` for the first, `elif` for the middle ones and `else` for the last:

```python
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
```

```output
The vegetable is yellow
```

Here we used `==` to test for equality. Python's comparison operators are: equality `==`, inequality `!=`, less than `<`, greater than `>`, less than or equal `<=` and greater than or equal `>=`. If you need to make multiple comparisons at the same time you use the logical operators `and`, `or` and `not`. Logical operators have lower precedence than the code that they are comparing. This means that sections of code will be calculated and then compared. 

Suppose we want to check whether a letter is a vowel. This requires checking against five possibilities which would make our if statement long. Instead, we can use the membership operator `in` to check:

```python
# Code 3
# Using in for multiple comparisons
vowels = 'aeiou'
letter = 'o'
letter in vowels
```

```output
True
```

Note that when using a dictionary, the `in` operator checks the keys of the dictionary:

```python
# Code 4
# Using in for a dictionary
vowel_dict = {'a': 'alpha', 'e': 'echo', 'i': 'india', 'o': 'oscar', 'u': 'uniform'}
letter = 'o'
letter in vowel_dict
```

```output
True
```

As of Python 3.8, we can use the walrus operator which takes the form `name := expression`. With this operator we can combine assignment and test tasks into a single line:

```python
# Code 5
# Using the walrus operator
temperature_1 = 30
temperature_2 = 50

if diff := abs(temperature_2 - temperature_1) >= 10:
    print("The two temperatures are very different.")
else:
    print("The two temperatures are close enough.")
```

```output
The two temperatures are very different.
```

This operator works equally well with `for` and `while`.
