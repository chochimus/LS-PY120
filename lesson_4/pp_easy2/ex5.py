class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        hello = Greeting()
        hello.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

Hello().hi()
hello = Hello()
hello.hi()