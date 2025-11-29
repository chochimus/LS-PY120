class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())
# First we create an instance of the Television class. We call its manufacturer class method
# printing "Amazon" then its model instance method printing "Omni Fire"


print(Television.manufacturer())
print(Television.model())

# Next we call the class method manufacterer directly on the class printing "Amazon" again
# Finally we try to call the instance method of Television directly on the class causing
# A TypeError as it needs an instance for the 'self' argument.