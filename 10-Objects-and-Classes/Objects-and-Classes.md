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

A new class initially inherits everything from its parent class. We can override any methods, including `init()`. Below is an example of us adding a new method to our subclass.

```python
# Code 4
# A new method to a subclass
class Person():
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name):
        self.name = "Dr. " + name

    def degree(self):
        return True

# Define a new person and show that they have a degree
person_A = Doctor("Bob Smith")
person_A.name, person_A.degree()
```

```output
('Dr. Bob Smith', True)
```

Consider we wanted to call a parent method. Here we define a new class EmailPerson that represents a Person that has an email.

```python
# Code 5
# Using super()
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
```

By defining an `init()` method for the subclass, we are replacing the `init()` method of its parent class. We could have defined our new class with `self.name = name`, but that would have defeated our use of inheritance. We used `super()` to make `Person()` do its work, the same as a plain Person object would. The other benefit is that if the definition of Person changes in the future, using `super()` will ensure that the attributes and methods that EmailPerson inherits from Person will reflect the change.

#### Multiple Inheritance

Objects can inherit from multiple classes. If your class refers to a method or attribute it does not have, Python will look in all the parents. If more than one of them has something with the same name, inheritance depends on the method resolution order. Each Python class has a special method called `mro()` that returns a list of the classes that would be visited to find a method or attribute for an object of that class. Consider the following class, its two child classes and the two classes derived from these.

```python
# Code 6
# Parent class - Animal
class Animal():
    def intro(self):
        return "I am an animal"
    
# Child class - Horse
class Horse(Animal):
    def intro(self):
        return "Neigh"
    
# Child class - Donkey
class Donkey(Animal):
    def intro(self):
        return "Hee-haw"
    
# Derived class - Mule (Father Donkey, Mother Horse)
class Mule(Donkey, Horse):
    pass

# Derived class - Hinny (Father Horse, Mother Donkey)
class Hinny(Horse, Donkey):
    pass
```

Assuming that a child speaks like its father, we can use `mro` to see the order the classes are searched and call their `intro()` method to see what they say:

```python
# Code 7
# Mule mro
Mule.mro()

# Hinny mro
Hinny.mro()

# What a mule says
mule = Mule()
mule.intro()

# What a hinny says
hinny = Hinny()
hinny.intro()
```

```output
[<class '__main__.Mule'>, <class '__main__.Donkey'>, <class '__main__.Horse'>, <class '__main__.Animal'>, <class 'object'>]
[<class '__main__.Hinny'>, <class '__main__.Horse'>, <class '__main__.Donkey'>, <class '__main__.Animal'>, <class 'object'>]
'Hee-haw'
'Neigh'
```

---

### Attribute access

Some object-oriented languages support private object attributes that can not be accessed directly from the outside. Python does not have private attributes but you can write *getters* and *setters* with obfuscated attribute names for privacy (the best solution is to use *properties*). Below is an example showing a name attribute with a setter and getter.

```python
# Code 8
# Class with a getter and setter for name
class Person():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('Inside getter')
        return self.hidden_name
    
    def set_name(self, input_name):
        print('Inside setter')
        self.hidden_name = input_name
```

```python
# Using the getter
bradley = Person('Bradley')
bradley.get_name()
```

```output
Inside getter
'Bradley'
```

```python
# Using the setter
bradley.set_name('Bradley Ward')
bradley.get_name()
```

```output
Inside setter
Inside getter
'Bradley Ward'
```

The Pythonic solution for attribute privacy is to use properties. There are two ways to do this, first is to add `name = property(get_name, set_name)` as the final line of the class definition, or you add some decorators:

`@property` goes before the getter method

`@name.setter` goes before the setter method.

```python
# Code 9
# Class with a property for private attributes
class Person():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('Inside getter')
        return self.hidden_name
    
    @name.setter
    def set_name(self, input_name):
        print('Inside setter')
        self.hidden_name = input_name
```

A property can also return a computed value. Let us define a Circle class that has a radius attribute and a computed diameter property.

```python

# Code 10
# A computed value set as a property
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2*self.radius

# Using our new attribute
c = Circle(5)
c.diameter
```

```output
10
```

If you do not specify a setter property for an attribute, you can not set it from the outside. This is useful for read-only attributes. In our `Person()` example above, the hidden attribute `hidden_name` was not completely hidden (it could still be called). By beginning an attribute's name with two underscores, the attribute will not be visible outside the class definition.

---

### Method types

Some methods are part of the class itself, some are part of the objects that are created from the class, and some are neither:

- If there is no preceding decorator, it is an *instance method*, and its first argument should be `self` to refer to the individual object itself.
- If there is a preceding `@classmethod` decorator, it is a *class method*, and its first argument should be `cls`, referring to the class itself.
- If there is a preceding `@staticmethod` decorator, it is a *static method*, and its first argument is neither an object or a class.

#### Instance methods

When you see an initial `self` argument in methods within a class definition, it is an instance method. These are the types of methods that you would normally write when creating your own classes. The first parameter of an instance method is `self`, and Python passes the object to the method when you call it. These are the ones defined thus far.