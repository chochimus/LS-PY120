class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?

# Without running you can see that the sparrow initializer only sets the color variable
# Printing species will return an AttributeError. The fix would be to call super.__init__(species)