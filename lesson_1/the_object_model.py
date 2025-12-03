# Exercise 1
"""
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. 
The class should have at least one instance variable that gets initialized by 
the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.

ANSWER:
We create a class by defining it using class followed by name of the class in PascalCase. 
Any attributes of the class should be defined within its body. To create an object
we call the class constructor such as Dog() 
"""

class Dog():
    def __init__(self, name):
        self.name = name
    
fido = Dog("Fido")
bob = Dog("Bob")

# Exercise 2
"""
Exercise 2
Given an instance of a Foo object, show two ways to print I am a Foo object
without hardcoding the word Foo.
"""

class Foo():
    pass

foo1 = Foo()
foo2 = Foo()
print(f'I am a {foo1.__class__.__name__}')
print(f'I am a {type(foo2).__name__}')