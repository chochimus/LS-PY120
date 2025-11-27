class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())

# This code will print roar. Reason being that when the class method make_sound is called
# it returns the class variable sound of the calling class. Because Lion sets its own sound 
# variable, this is the one that is used.