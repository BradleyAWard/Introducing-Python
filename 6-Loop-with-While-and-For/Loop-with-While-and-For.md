## 5) Loop with While and For

Testing with `if`, `elif` and `else` runs from top to bottom. Often, we need to do something more than once, requiring a loop. Python gives us two options for generating loops: `while` and `for`.

---

The simplest looping mechanism in Python is `while`. Below is a simple `while` example:

```python
# Code 1
# A simple while loop
count = 1
while count <= 5:
    print(count)
    count += 1
```

```output
1
2
3
4
5
```

If you want to loop until something occurs, but not sure when that might happen, we can use an infinite loop with a `break` statement:

```python
# Code 2
# Break out of a while loop
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 5:
        break
```

```output
1
2
3
4
```

Sometimes we do not want to break out of a loop but skip ahead to the next iteration. We can move on to the next iteration using `continue`:

```python
# Code 3
# Skip iterations with continue
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 5:
        count += 2
        continue
```

```output
1
2
3
4
7
8
9
10
```

Python makes frequent use of iterators that make it possible to traverse data structures without knowing how large they are or how they are implemented. One can even iterate over data that is created on the fly, allowing processing of data streams that would otherwise not fit into the computer's memory all at one.

We can generate a stream of numbers within a specific range using the `range()` function. Like `zip()`, `range()` returns an iterable object, so you need to step through the values with `for` ... `in`, or convert the object to a sequence like a list. As a simple example:

```python

# Code 4
# Using range()
for x in range(2, 10, 2):
    print(x)
```

```output
2
4
6
8
```