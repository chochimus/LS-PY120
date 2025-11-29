class Animal:
    def speak(self, sound):
        print(sound)

class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    def bark(self):
        self.speak(("Woof! " * 3).strip())

bob = Cat()
bob.meow()

dylan = Dog()
dylan.bark()