class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

# Its type will be Pine Tree. The super call initially sets the instance variable type to
# 'Generic Tree', but it is overwritten in the next step to 'Pine Tree'

pine = Pine()
print(pine.type)