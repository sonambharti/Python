from abc import ABC, abstractmethod

class Vehicle(ABC):  # Vehicle is an abstract base class
    @abstractmethod
    def drive(self):
        pass
    

class Car(Vehicle):
    def drive(self):
        return "The car is driving on the road."

class Boat(Vehicle):
    def drive(self):
        return "The boat is sailing on the water."

# Cannot instantiate abstract class directly
# vehicle = Vehicle()  # This would raise a TypeError

car = Car()
boat = Boat()

print(car.drive())
print(boat.drive())
