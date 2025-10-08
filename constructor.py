class Car:
    def __init__(self):

        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

car = Car()
print(car.make)
print(car.model)
print(car.year)


class Car:
    def __init__(self, make, model, year):
      
        self.make = make
        self.model = model
        self.year = year

car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)

#destructor
class Employee:

    def __init__(self):
        print('Employee created.')

    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj

