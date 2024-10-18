## 7) Tuples and Lists

We have already looked at strings which are sequences of characters. Python has two other sequence structures: tuples and lists. These contain zero or more elements. Unlike strings, the elements can be any Python object. Tuples are immutable; when you assign elements (only once), to a tuple, they cannot be changed. Lists are mutable, meaning you can insert and delete elements at will.

---

### Tuples

To make a tuple with one or more elements, follow each element with a comma. We can unpack a tuple using commas as well.

```python
# Code 1
# An example tuple
name = ('Joe', 'Edward', 'Bloggs')
forename, middle, lastname = name
print(forename)
```

```output
Joe
```

