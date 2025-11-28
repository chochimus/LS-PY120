class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
small_car.go_fast()
# I am a super fast Car!

# The vehicle type is output because self.__class__.__name__ refers to the class instance
# that is calling the method. self -> small_car    __class__ -> Car class referece
#  __name__ -> 'Car'