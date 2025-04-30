## 8) Dictionaries and Sets

### Dictionaries

A dictionary is similar to a list, but the order of the items does not matter and they are not selected by an offset. Instead, we specify a unique key to associate with each value. The key is often a string, but can be any of Python's immutable types. Dictionaries are mutable so we can add, delete and change key-value elements. To create a dictionary we use curly brackets around comma separated key:value pairs.

```python
# Code 1
# An example dictionary
dictionary = {'A': 1,
              'B': 2,
              'C': 3}
```

We add items to dictionaries by referring to the item by its key and assign a value. If the key was already present, the existing value is replaced, otherwise it is added to the dictionary with its value. If you use a key more than once, the last value is shown.

We can get an item from a dictionary by specifying the dictionary and a key to get the corresponding value. If the key is not in the dictionary it will raise a KeyError. We can avoid this using the `get()` function. We provide the dictionary, key and an optional value which occurs if the key is not found:

```python
# Code 2
# Using the get() function
dictionary.get('D', 'Not in the dictionary')
```

```output
'Not in the dictionary'
```

We can get all the keys in a dictionary using the `keys()` function, the values using `values()` and all key-value paits using `items()`.

```python
# Code 3
# Using the keys() method
print(dictionary.keys())

# Using the values() method
print(dictionary.values())

# Using the items() method
print(dictionary.items())
```

```output
dict_keys(['A', 'B', 'C'])
dict_values([1, 2, 3])
dict_items([('A', 1), ('B', 2), ('C', 3)])
```

As of Python 3.5 there is a new way to merge dictionaries using `**`. Consider the following dictionaries:

```python
# Code 4
# Combining dictionaries
dict1 = {'A': 1,
         'B': 2,
         'C': 3}

dict2 = {'D': 4,
         'E': 5,
         'F': 6}

dict3 = {'G': 7,
         'H': 8,
         'I': 9}

combined_dict = {**dict1, **dict2, **dict3}
combined_dict
```

```output
{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9}
```

There are two ways that we can copy a dictionary. To copy keys and values from a dictionary to another dictionary we can use `copy()`. This is a shallow copy and works if the dictionary values are immutable. If they are not, we need `deepcopy()`. Much like lists and tuples, dictionaries can be compared with the operators `==` and `!=`. Python compares the keys and values one by one; the order in which they were originally created does not matter.

Iterating over a dictionary returns the keys. To iterate over the values rather than the keys, you use the dictionary's `values()` function, and to return both the key and the value as a tuple, you can use the `items()` function. Examples of all three are below:

```python
# Code 5
# Iterating over keys
for key in dict1:
    print(key)

# Iterating over values
for value in dict1.values():
    print(value)

# Iterating over items
for item in dict1.items():
    print(item)
```

```output
A
B
C

1
2
3

('A', 1)
('B', 2)
('C', 3)
```

#### Dictionary Comprehension

As with lists there are also dictionary comprehension which take the form:

`{key_expression: value_expression for expression in iterable}`

Dictionary comprehensions can also include conditional statements of the form:

`{key_expression: value_expression for expression in iterable if condition}`

```python
# Code 6
# Example dictionary comprehension
vowels = 'aeiou'
word = 'onomatopoeia'

letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

vowel_counts = {letter: word.count(letter) for letter in word if letter in vowels}
print(vowel_counts)
```

```output
{'o': 4, 'n': 1, 'm': 1, 'a': 2, 't': 1, 'p': 1, 'e': 1, 'i': 1}
{'o': 4, 'a': 2, 'e': 1, 'i': 1}
```

---

### Sets

A set is like a dictionary without its values, leaving only the keys. As with a dictionary, each key must be unique. You use a set when you only want to know that something exists and nothing else about it. To create a set we use the `set()` function or enclose one or more comma separated values in urly brackets. Note however that `{}` does not create an empty set but an empty dictionary.

```python
# Code 7
# Defining a set
set('letters')
```

```output
{'t', 'l', 's', 'r', 'e'}
```

Note how the set records just one item despite the letters *t* and *e* appearing twice. We can get the length of the set with `len()`, add an item with `add()` and delete an item with `remove()`. A common use for a set is to define a dictionary where the values are the sets. Consider the following dictionary of drinks and their ingredients. We can use this to find what drinks contain particular ingredients.

```python
# Code 8
# Example dictionary with sets as values
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# Find keys in dictionary based on their set
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
```

```output
martini
black russian
white russian
screwdriver
```

If we wish to check for combinations of set values we use the set intersection operator `&`. Suppose we want to find any drink that has orange juice or vermouth:

```python
# Code 9
# Find keys in dictionary based on combinations of set values
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
```

```output
martini
manhattan
screwdriver
```

The following are examples of more set operators. Some have special punctuation, some have special functions, and some have both. The intersection (members common to both sets) are prescribed with `&` and the union (members of either set) are found by using `|`. The difference (members of the first set but not the second) is obtained using the character `-`. and the exclusive or (items in one set or the other, but not both) uses `^`.

```python
# Code 10
# Define two different sets
a = {1, 2, 3}
b = {2, 3, 4}

# In both A and B
a & b

# A or B
a|b

# In A but not in B
a - b

# In A or B but not both
a ^ b
```

```output
{2, 3}
{1, 2, 3, 4}
{1}
{1, 4}
```

#### Set Comprehension

Set comprehensions can be made using the following form:

`{expression for expression in iterable}`,

and can have an optional conditional of the form:

`{expression for expression in iterable if condition}`

```python
# Code 11
# An example set comprehension
a_set = {number for number in range(1, 6)}
print(a_set)

# An example set with condition
b_set = {number for number in range(1, 6) if number % 3 == 1}
print(b_set)
```

```output
{1, 2, 3, 4, 5}
{1, 4}
```
