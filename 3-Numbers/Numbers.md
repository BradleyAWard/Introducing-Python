## 3) Numbers

We shall begin by looking at Python's simplest built-in data types: Booleans, Integers and Floats. In Python the only values for the boolean data type are True and False. You can convert any Python data type to a boolean using the function `bool()`, where any non-zero number is considered True and zero-valued ones are considered False. Integers are whole numbers and bases (if you want to express numbers in ways other than the usual decimal base 10).

---

### Operations

There are a range of operations we can perform with integers, summarized by the operators in the list below:

| Operation | Symbol |
| -- | -- |
| Addition | + |
| Subtraction | - |
| Multiplication | * |
| Floating-point division | / |
| Integer division | // |
| Modulus | % |
| Exponentiation | ** |

If we wish to reassign an existing variable to an arithmetic function of its earlier version, we can combine these operators with the equal sign:

```python
# Code 1
# Applying arithmetic functions
a = 10
a -= 5
print(a)

a = 10
a += 5
print(a)

a = 10
a *= 5
print(a)

a = 10
a /= 5
print(a)

a = 10
a //= 5
print(a)
```

```output
5
15
50
2.0
2
```

---

### Bases

Integers are assumed to be decimal (base 10) unless a prefix is used to specify another base. In Python you can express integers in three other bases.

- 0b or 0B for binary (base 2)
- 0o or 0O for octal (base 8)
- 0x or 0X for hex (base 16)

The following illustrate what 10 would be interpreted as in all the allowed Python bases:

```python
# Code 2
# Decimal base
print(10)

# Binary base
print(0b10)

# Octal base
print(0o10)

# Hexadecimal base
print(0x10)
```

```output
10
2
8
16
```

---

### Type conversions

To change other Python data types to an integer we can use the `int()` function. This is particularly useful on booleans to convert True to 1 and False to 0. Similarly, the `bool()` function will convert  the value 1 to True and 0 to False. The same functions also apply to floats (e.g. `float()`).

```python
# Code 3
# Convert boolean to integer
print(int(True), int(False))

# Convert integer to boolean
print(bool(1), bool(0))
```

```output
1 0
True False
```