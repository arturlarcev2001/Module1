

class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000
    def horse_powers(self):
        return self.powers

class Nissan(Car, Vehicle):
    vehicle_type = "sedan"
    price = 2000000
    def horse_powers(self, powers):
        return powers

car = Nissan
print(car.vehicle_type)
print(car.price)
