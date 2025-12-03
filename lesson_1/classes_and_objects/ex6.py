# Exercise 6

"""
Going back to your solution to exercise 1, refactor the code to replace 
any methods that can be converted to static methods. Once you have done that, 
ask yourself whether the conversion to a static method makes sense.
"""

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
    @staticmethod
    def engine_on():
        print("engine on")
    def accelerate(self, speed):
        self.speed += speed
        print("accelerating")
    def brake(self, speed):
        if self.speed - speed < 0:
            self.speed = 0
        else:
            self.speed -= speed
        print("braking...")
    def engine_off(self):
        self.speed = 0
        print("engine off")
    def get_speed(self):
        print(f'Your speed is: {self.speed}')

car = Car("BMW", 1996, "Red")
Car.engine_on()
car.accelerate(10)
car.get_speed()
car.brake(10)
car.engine_off()