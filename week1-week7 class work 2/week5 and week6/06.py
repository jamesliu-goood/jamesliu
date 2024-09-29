class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

    def display_info(self):
        print(f"Car Info: {self.year} {self.color} {self.model}")


my_car = Car('blue', 'Ford Mustang', 2021)

my_car.drive()
my_car.stop()
my_car.display_info()