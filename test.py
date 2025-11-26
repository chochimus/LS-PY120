# TODO 
"""
need to go back through lesson one and add exercises to repository
also create a new repo for small problems
"""

class FarmAnimal:
    def speak(self):
        return f'{self.__class__.__name__} says '

class Sheep(FarmAnimal):
    def speak(self):
        return super().speak() + 'baa!'

class Lamb(Sheep):
    def speak(self):
        return 'baaaaaaa!'

class Cow(FarmAnimal):
    def speak(self):
        return super().speak() + 'mooooooo!'

print(Sheep().speak())        # Sheep says baa!
print(Lamb().speak())         # Lamb says baa!baaaaaaa!
print(Cow().speak())          # Cow says mooooooo!