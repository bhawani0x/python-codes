from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        print("Vehicle")

    def stop(self):
        print("Stop Vehicle")


class motorcycle(Vehicle):
    def go(self):
        print("Motorcycle")

    def stop(self):
        print("Stop motorcycle")


class car(Vehicle):
    def go(self):
        print("Car")


# v = Vehicle()  # we can not create object from vehicle class because it is abstract class
# v.go()

m = motorcycle()
# m.go()
m.stop()

c = car()
c.go()
c.stop()
