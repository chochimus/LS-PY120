# TODO 
"""
need to go back through lesson one and add exercises to repository
also create a new repo for small problems
"""

class SpeedyMixin:
    def run_fast(self):
        self.speed = 70

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    DOG_YEARS = 7

    def __init__(self, name, age):
        self.dog_age = age * Dog.DOG_YEARS

class Greyhound(SpeedyMixin, Dog):
    pass

grey = Greyhound('Grey', 3)
print(grey.age)