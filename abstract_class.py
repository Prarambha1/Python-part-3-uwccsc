"""
abstract class: a class that canot be instantiated on its own; meant to be subclassed.
They can contain abstract methods, which are declared but have no implementation.
abstract class benefits:
1) prevents instantiation of the class itself
2) requires children to use inherited abstract methods
"""

from abc import ABC, abstractmethod #Abstract Base Class

class vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

     
class car(vehicle):
    
    def go(self):
        print("drive the car")
    
    def stop(self):
        print("stop it")

class Motorcycle(vehicle):
    def go(self):
        print("ride the motorcycle")
    
    def stop(self):
        print("stop it")

class boat(vehicle):
    def go(self):
        print("sail the boat")

    def stop(self):
        print("stop it")

car = car()
car.go()
car.stop()

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

boat = boat()
boat.go()
boat.stop()

