class Cat:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() != other.name.casefold()
    
fluffy = Cat("fluffy")
fluffy2 = Cat("FLUFFY")
bob = Cat("bob")

print(fluffy == fluffy2) # True
print(bob == fluffy)     # False

print(fluffy != bob)     # True
print(fluffy != fluffy2) # False