

class Car:
    price = 1000000
    def horse_powers(self):
        return self.powers

class Nissan(Car):
    price = 2000000
    def horse_powers(self, powers):
        return powers

class Kia(Car):
    price = 3000000
    def horse_powers(self, powers):
        return powers

c = Car()
n = Nissan()
k = Kia()
print(c.price)
print(n.price)
print(n.horse_powers(1000))
print(k.price)
print(k.horse_powers(2000))
    
