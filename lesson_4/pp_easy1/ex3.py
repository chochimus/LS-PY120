class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')


# If we want them to go fast, we inherit from the SpeedMixin class. This gives them access
# To the method

car = Car()
truck = Truck()

car.go_fast()
truck.go_fast()