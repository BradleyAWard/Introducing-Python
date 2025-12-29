## 10) Objects and Classes

An object is a custom data structure containing both data (variables called attributes) and code (functions called methods). Unlike modules, you can have multiple objects (referred to as instances) at the same time, each with potentially different attributes.

To create a new object that no one has ever created before, you first define a class that indicates what it contains. Suppose that you want to define objects to represent information about cats. Each object will represent a single cat. Below is the simplest example of the Cat class. We can create an instance of a cat and assign a few attributes to our first object.

```python
# Code 1
# A simple class for cats
class Cat():
    pass

# An example cat
cat_a = Cat()
cat_a.name = "Fred"
cat_a.age = 4
```

A method is a function in a class or object. A method looks like any other function, but can be used in special ways. If you want to assign object attributes at creation time, you need the special Python object initialization method `init()`. When you define `init()` in a class definition, its first parameter should be named `self`. The `self` argument specifies that it refers to the individual object itself.

```python
# Code 2
# A class with name initialized at __init__()
class Cat():
    def __init__(self, name):
        self.name = name

# An example cat
cat_b = Cat("Grumpy")
```

This new object is like any other object in Python, it can be used as an element of a list, tuple, dictionary or set. You can pass it to a function as an argument or return it as a result. It is not necessary to have an `init()` method in every class definition; it is used to do anything that is needed to distinguish this object from other created from the same class.

---

### Inheritance

When trying to solve a problem we will often have an existing class that creates objects that do almost what you need. We could then modify this class, but it will make it more complicated and corrupt something that used to work. We cold write a new class, copying from the original class, but this means more code to maintain and the parts of the old and new class that used to work the same might drift apart because they are in separate places. The solution is inheritance: creating a new class from an existing class, but with some additions or changes. When you use inheritance, the new class automatically uses all the code from the old class.

You define only what you need to change or add in the new class, and this overrides the behavior of the old class. The original class is called a *parent*, *superclass* or *base class* and the new class is called a *child*, *subclass* or *derived class*. Below is an example of a subclass:

```python
# Code 3
# An animal superclass and cat subclas
class Animal():
    pass

class Cat(Animal):
    pass

# Check that cat is a subclass of animal
issubclass(Cat, Animal)
```

```output
True
```