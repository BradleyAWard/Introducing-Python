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

Here we used `==` to test for equality. Python's comparison operators are: equality `==`, inequality `!=`, less than `<`, greater than `>`, less than or equal `<=` and greater than or equal `>=`. If you need to make multiple comparisons at the same time you use the logical operators `and`, `or` and `not`.
