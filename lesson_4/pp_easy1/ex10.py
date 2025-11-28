class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
    
# _cats_count is a class variable that keeps track of how many Cats instances are created. 
# When the initializer is ran, the class variable is incremented by 1.

cat = Cat('black')
cat2 = Cat('orange')

print(cat.cats_count()) # 2
print(cat2.cats_count()) # 2