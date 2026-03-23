# Code 1
# A simple class for cats
class Cat():
    pass

# An example cat
cat_a = Cat()
cat_a.name = "Fred"
cat_a.age = 4

# Code 2
# A class with name initialsized at __init__()
class Cat():
    def __init__(self, name):
        self.name = name

# An example cat
cat_b = Cat("Grumpy")

# Code 3
# An animal superclass and cat subclas
class Animal():
    pass

class Cat(Animal):
    pass

# Check that cat is a subclass of animal
issubclass(Cat, Animal)

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

# Code 5
# Using super()
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

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

# Using the getter
bradley = Person('Bradley')
bradley.get_name()

# Using the setter
bradley.set_name('Bradley Ward')
bradley.get_name()

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

# Code 11
# Defining a class method
class Person():
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    @classmethod
    def counter(cls):
        print("There are", cls.count, "people")

# Using the class method
person_a = Person("Bob", 24)
person_b = Person("Alan", 27)
person_c = Person("George", 21)
Person.counter()

# Code 12
# Defining a static method
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def exclaim():
        print("I am human")

# Using the static method
Person.exclaim()

# Code 13
# Defining the __eq__() magic method
class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    
# Creating three words
first_word = Word("Hello")
second_word = Word("hello")
third_word = Word("Hi")

# Comparing the three words
first_word == second_word, second_word == third_word, first_word == third_word