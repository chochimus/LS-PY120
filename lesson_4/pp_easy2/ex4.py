class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# Snippet 1
# hello = Hello()
# hello.hi()
# prints "Hello"

# Snippet 2
# hello = Hello()
# hello.bye()
# AttributeError , Hello/Greeting have no method called bye

# Snippet 3
# hello = Hello()
# hello.greet()
# TypeError, greet takes a string argument message

# Snippet 4
# hello = Hello()
# hello.greet('Goodbye')
# prints "Goodbye"

# Snippet 5
# Hello.hi()
# Error, hi is not a classmethod and requires an instance to be used in self