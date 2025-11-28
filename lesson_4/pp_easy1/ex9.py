excited_dog = 'excited dog'
self.excited_dog = 'excited dog'
self.__class__.excited_dog = 'excited dog'
BigDog.excited_dog = 'excited dog'

# first is a regular local variable
# second is the instance variable the object referred to by self, denoted by the self. prefix
# third would be the class variable in the class of the object referred to by self 
#   denoted by the self.__class__. prefixes
# fourth would refer to the class variable in the BigDog class, denoted by the class name
#   as the prefix