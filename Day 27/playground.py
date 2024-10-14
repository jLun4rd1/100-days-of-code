def add(*args:int):
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum

print(add(1,2,3,4,5,6,7,8,9,10))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs['add'])
    # print(kwargs['multiply'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    
calculate(2, add=3, multiply=5)

class Car:
    
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get("model")
        
my_car = Car(make='Nissan', model='GT-R')
print(my_car.make)
print(my_car.model)