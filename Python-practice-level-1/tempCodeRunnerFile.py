
class Car:
    @staticmethod
    def start():
        print("car started!")

    @staticmethod
    def stop():
        print("car stopped!")

class ToyotaCar(Car): # child class
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner") # object creation
car2 = ToyotaCar("Innova")  # object creation

print(car1.name) # Output: Fortuner
print(car2.name) # Output: Innova

print(car1.start()) # Output: car started!
print(car2.stop()) # Output: car stopped!