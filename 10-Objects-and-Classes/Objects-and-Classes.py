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