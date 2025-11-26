class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
rect = Rectangle(1, 2)
print(rect.width)
print(rect.height)

# rect.width = 2 AttributeError
# rect.height = 3 AttributeError