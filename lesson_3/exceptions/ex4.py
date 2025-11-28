
input = int(input("Enter a number: "))
if input < 0:
    raise ValueError("Number must be positive")
print(input)