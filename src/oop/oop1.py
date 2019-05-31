# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#MAIN Base class
class Vehicle:
    pass

#Flying Base class    
class FlightVehicle(Vehicle):
    pass
#flying child
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass        

#Ground Base class
class GroundVehicle(Vehicle):
    pass
#ground child
class Car(GroundVehicle):
    pass
class Motorcycle(GroundVehicle):
    pass
