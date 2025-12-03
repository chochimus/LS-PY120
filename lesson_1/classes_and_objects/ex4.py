# Exercise 4

"""
Add a class method to your Car class that calculates and prints any car's
average gas mileage (miles per gallon). You can compute the mileage by
dividing the distance traveled (in miles) by the fuel burned (in gallons).
"""

class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0

    @classmethod
    def average_gas_mileage(cls, distance, fuel_burned):
        try:
            print(distance/fuel_burned)
        except ZeroDivisionError:
            print("Sorry your car is empty")
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

    def spray_paint(self, color):
        self.color = color

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
car.spray_paint("Purple")
print(car.color)
Car.average_gas_mileage(10, 5)
Car.average_gas_mileage(10, 0)