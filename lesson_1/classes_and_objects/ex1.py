# Exercise 1

"""
Create a Car class that meets these requirements:

- Each Car object should have a model, model year, and color provided 
at instantiation time.
- You should have an instance variable that keeps track of the current speed. 
Initialize it to 0 when you instantiate a new car.
- Create instance methods that let you turn the engine on, accelerate, brake, 
and turn the engine off. Each method should display an appropriate message.
- Create a method that prints a message about the car's current speed.
- Write some code to test the methods.
"""

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
    def engine_on(self):
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
car.engine_on()
car.accelerate(10)
car.get_speed()
car.brake(10)
car.engine_off()