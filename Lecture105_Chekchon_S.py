class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirCondition(self):
        print("Turn on : Air")
class PickUp(Vehicle):
    pass
class Car(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass
pickup = PickUp()
pickup.turnOnAirCondition()

car = Car()
car.turnOnAirCondition()

van = Van()
van.turnOnAirCondition()

estatecar = Estatecar()
estatecar.turnOnAirCondition()