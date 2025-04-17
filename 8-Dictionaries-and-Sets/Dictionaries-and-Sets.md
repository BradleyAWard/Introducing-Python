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

{key_expression: value_expression for expression in iterable}
