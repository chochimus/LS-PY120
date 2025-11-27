class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# When you initialize B you don't call super().__init__() so the initalizer for the instance
# variables in A are never set for B objects and the print will result in an AttributeError.