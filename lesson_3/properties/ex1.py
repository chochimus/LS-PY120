class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        
        self._name = name

bob = Person('Bob')
print(bob.name)

bob.name = "notbob"
print(bob.name)

bob.name = 123