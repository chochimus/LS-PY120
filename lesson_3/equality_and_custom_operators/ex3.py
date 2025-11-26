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
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() < other.name.casefold()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() <= other.name.casefold()
    
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() > other.name.casefold()
    
    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() >= other.name.casefold()
    
fluffy = Cat("fluffy")
fluffy2 = Cat("FLUFFY")
bob = Cat("bob")
abacus = Cat("abacus")

print(fluffy == fluffy2) # True
print(bob == fluffy)     # False

print(fluffy != bob)     # True
print(fluffy != fluffy2) # False

print(fluffy > abacus)   # True
print(abacus >= bob)     # False

print(abacus < bob)      # True
print(fluffy <= bob)     # False