# Exercise 2

"""
Using decorators, add getter and setter methods to your Car class so you can 
view and change the color of your car. You should also add getter methods 
that let you view but not modify the car's model and year. 
Don't forget to write some tests.
"""

class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
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

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        self._color = new_color
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

car = Car("BMW", 1996, "Red")
car.engine_on()
car.accelerate(10)
car.get_speed()
car.brake(10)
car.engine_off()
car.color = "Green"
print(car.color)
print(car.model)
print(car.year)