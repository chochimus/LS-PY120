class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

# Pizza will create objects that have instance variables. This is because of the self prefix,
# without it the variable is only local to the scope of the function itself.