class NegativeNumberError(ValueError):
    def __init__(self, *args):
        super().__init__(*args)


input = int(input("Enter a number: "))
if input < 0:
    raise NegativeNumberError("Number must be positive")
print(input)