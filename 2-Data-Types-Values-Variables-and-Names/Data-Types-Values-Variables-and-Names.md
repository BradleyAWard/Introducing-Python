## 2) Data - Types, Values, Variables and Names

We begin with Python's data types and the values that they can contain. Then we see how to represent data as literal values and variables.

---

### Types

Below is a table that shows the basic data types in Python. The column *mutable* indicates whether the values can be changed after creation.

| Name | Type | Mutable |
| -- | -- | -- |
| Boolean | bool | No |
| Integer | int | No |
| Floating point | float | No |
| Complex | complex | No |
| Text string | str | No |
| List | list | Yes |
| Tuple | tuple | No |
| Bytes | bytes | No |
| BytesArray | bytearray | Yes |
| Set | set | Yes |
| Frozen set | frozenset | No |
| Dictionary | dict | Yes |

---

### Variables

There are certain rules that are to be followed in the naming of variables. Python variables may only contain lowercase letters, uppercase letters, digits and underscores. They are case-sensitive and they must not begin with a digit. Names that begin with an underscore are treated differently and they cannot be one of Python's reserved words (known as keywords). You can find a list of the keywords using: 

```python
# Code 1
help("keywords")
```

```output
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not 
```

Remember that assignment of a variable does not copy a value, it attaches a name to the object that contains the data. The name is a reference to a thing rather than the thing itself. If we wish to know the type of a variable we can use `type()`. If an object is immutable (like an integer), it's value cannot be changed, so assigning two names to an object means they are essentially read-only. But if both names point to a mutable object, you can change the object's value via either name and you will see the changed value when looking up either variable names. See the below example using lists:

```python
# Code 2
# Name assignment for mutable objects
a = [2, 4, 6]
b = a
print(a, b)
```

```output
[2, 4, 6] [2, 4, 6]
```

```python
# Code 3
# After making a change to one list
a[0] = 99
print(a, b)
```

```output
[99, 4, 6] [99, 4, 6]
```