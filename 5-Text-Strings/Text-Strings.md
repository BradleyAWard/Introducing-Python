## 5) Text Strings

Unlike other languages, strings in Python are immutable. You cannot change a string in place, but you can copy parts of strings to another string to get the same effect. Python has a variety of types of strings, indicated by the letter before the first quote. `f` or `F` starts and f-string which is used for formatting. `r` or `R` starts a raw string and is used to prevent escape sequences in the string. The combination `fr` or `FR` starts a raw f-string, and a u-string starts a unicode string, which is the same as a plain string.

Python lets us escape the meaning of some characters within strings to achieve something that would otherwise be difficult to express. For example, the most common escape sequence is `\n` which begins a new line. Similarly, `\t` is used as a tab for aligning text. Note, however, that a raw string negates escape sequences, so will be printed exactly as written.

---

### Slicing, splitting and joining

We can extract part of a string using a slice. We define a slice using square brackets, a start value, an end value and an optional step count between them. Some of these values can be omitted as follows:

- `[:]` extracts the entire sequence from start to end.
- `[start:]` specifies from the start offset to the end.
- `[:end]` specifies from the beginning to the end offset (minus 1).
- `[start:end]` specifies from the start offset to the end offset (minus 1).
- `[start:end:step]` specifies from the start offset to the end offset (minus 1), skipping every step elements.

Using a negative step size we can step backwards through a string, for example:

```python
# Code 1
# Using a negative step count
name = "Joe Bloggs"
name[::-1]
```

```output
'sggolB eoJ'
```

We can use the built-in `split()` function to break a string into a list of small strings based on some operator. The opposite method is `join()` which collapses a list of strings into a single string:

```python
# Code 2
# Using the split() and join() functions
string_numbers = '1, 2, 3, 4, 5'
list_numbers = string_numbers.split(',')
print(list_numbers)

string_numbers = ','.join(list_numbers)
print(string_numbers)
```

```output
['1', ' 2', ' 3', ' 4', ' 5']
'1, 2, 3, 4, 5'
```

It is common to want to drop the leading or trailing padding characters from a string. The `strip()` function allows you to get rid of whitespace characters (`' '`, `'\t'`, `'\n'`). `strip()` strips both ends, `lstrip()` strips only from the left and `rstrip()` only from the right. Other methods that can be used on strings include: `capitalize()`, `title()`, `upper()`, `lower()` and `swapcase()`, which can all be seen below:

```python
# Code 3
# String manipulation functions
name = "My name is Joe Bloggs"

print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase())
```

```output
My name is joe bloggs
My Name Is Joe Bloggs
MY NAME IS JOE BLOGGS
my name is joe bloggs
mY NAME IS jOE bLOGGS
```

---

### Formatting strings

Python has three ways of formatting strings: old style (supported in Python 2 and 3), new style (Python 2.6 and newer) and f-strings (Python 3.6 and newer). We shall discuss the second two methods. The new style of formatting follows the format `format_string.format(data)`. The arguments to the `format()` function need to be in the same order as the `{}` placeholders in the format string:

```python
# Code 4
# String formatting with {} and .format()
name = "Joe Bloggs"
age = "30"

"My name is {} and I am {} years old".format(name, age)
```

```output
'My name is Joe Bloggs and I am 30 years old'
```

With the new style of formatting we can specify the arguments by position or by name:

```python
# Code 5
# String formatting by position and name
"My name is {0} and I am {1} years old".format(name, age)
"My name is {name} and I am {age} years old".format(name=name, age=age)
```

```output
'My name is Joe Bloggs and I am 30 years old'
'My name is Joe Bloggs and I am 30 years old'
```

f-strings appeared in Python 3.6 and are now the recommended way of formatting strings. To make an f-string, type the letter *f* before the initial quote and include variable names or expressions within `{}` to get their values into the string. The difference from the previous method is that the things that would normally be in the `.format()` can now be passed directly to the main string.

```python
# Code 6
# Using an f-string
f"My name is {name} and I am {age} years old"
```

```output
'My name is Joe Bloggs and I am 30 years old'
```