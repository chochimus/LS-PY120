class Car:
    manufacturer = 'BMW'

    def __init__(self):
        self.manufacturer = 'Ford'

    def show_manufacturer(self):
        print(f'{Car.manufacturer=}')
        print(f'{self.manufacturer=}')

car = Car()
car.show_manufacturer()
