# Exercise 3

"""
Add a method to the Car class that lets you spray paint the car a specific color. 
Don't use a setter method for this. Instead, create a method whose name accurately
describes what it does. Don't forget to test your code.
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