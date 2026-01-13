def add(*args):
    return sum(args)

print(add(1,2,3,4,5,6,7,8,9))

def calculate(n, **kwargs):
    print(n)
    return sum(kwargs.values())

print(calculate(a=1, b=2, c=3, n=12))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs["model"]
        self.year = kwargs.get('year')

my_car = Car(make="Toyota", model="M", year=2020)
print(my_car.make)
print(my_car.model)
print(my_car.year)