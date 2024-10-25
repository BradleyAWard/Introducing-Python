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

We can create a tuple from other things using the `tuple()` function.

```python
# Code 2
# Using the tuple() function
name = ['Joe', 'Edward', 'Bloggs']
tuple(name)
```

```output
('Joe', 'Edward', 'Bloggs')
```

We can concatenate tuples using `+` and duplicate items using `*`, but tuples are immutable so we can not modify the tuple. We can use concatenation to make a new tuple and reassign it with the same variable name so it appears to have been modified, but in reality they are two separate tuples.

---

### Lists

Lists are good for keeping track of things by their order, especially when the order or contents may change. Unlike strings and tuples, lists are mutable. They are made from zero or more elements, separated by commas and surrounded by square brackets. If you want to keep track of only unique values and do not care about order, a Python set might be a better choice that a list.

As with strings, we can extract a single value from a list by specifying its offset. We can also extract a sequence of a list using a slice, as we did for the `range()` function.

```python
# Code 3
# Slicing a list
count = [0, 1, 2, 3, 4, 5]
count[0:2]
```

```output
[0, 1]
```

We can reverse a list by not specifying the start or end values, but assigning the step value as -1. To reverse the list itself, rather than generating a new list, we can use the `.reverse()` method:

```python
# Code 4
# Reversing a list
print(count[::-1])
count.reverse()
print(count)
```

```output
[5, 4, 3, 2, 1, 0]
[5, 4, 3, 2, 1, 0]
```

We can add elements to lists using the `append()` and `insert()` functions. The `append()` function adds items one by one to the end of the list, the `insert()` function requires an index as the first argument to signify where the object should go in the list. We can also merge two lists together by using `extend()`.

To delete items in a list we can use `del`. When you delete an item by its position (i.e. `del list[-1]`), the items that follow move back to take the deleted items space and the list's length decreases by one. If you are not sure or do not care where the item is in the list, use `remove()` to delete it by value. If you had duplicate list items with the same value, `remove()` deletes only the first one it finds.

We can also return the index of a particular element in a list using `index()`, test for a value in a list using `in` and count the occurrences of a value with `count()`. Note that the `index()` method will only return the first correct value found in the list.

We will often need to sort items in a list by their values rather than their index. Python provides two functions: the list method `sort()` sorts the list itself in place; and the general function `sorted()` returns a sorted copy of the list. The default sort order is ascending, but you can add the argument `reverse = True` to set it to descending.

We can iterate over multiple sequences in parallel by using the `zip()` function. `zip()` stops when the shortest sequence is done:

```python
# Code 5
# Using zip() for iteration
names = ['Bob', 'Fred', 'James', 'Neal']
ages = [20, 24, 27, 19]
salaries = ['30,000', '40,000', '35,000']

for name, age, salary in zip(names, ages, salaries):
    print(name, "is", age, "and has a salary of", salary, "pounds")
```

```output
Bob is 20 and has a salary of 30,000 pounds
Fred is 24 and has a salary of 40,000 pounds
James is 27 and has a salary of 35,000 pounds
```

#### List comprehension

The most Pythonic way to create a list is by using a list comprehension. The simplest form of list comprehension looks like this:

`[expression for item in iterable]`

The list comprehension move a for loop inside the square brackets. A list comprehension can include a conditional expression which would have the form:

`[expression for item in iterable if condition]`

```python
# Code 6
# An example list comprehension
comprehension = [number for number in range(1, 6) if number % 2 == 1]
comprehension
```

```output
[1, 3, 5]
```

You might expect that changing the square brackets to parentheses would create a *tuple comprehension*. It would appear to work because there is no exception, but the line between the parenthesis would actually be a generator comprehension, and it returns a generator object. A generator is one way to provide data to an iterator.