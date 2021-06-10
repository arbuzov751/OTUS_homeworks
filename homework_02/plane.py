"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight=1200, fuel=0, fuel_consumption=7, max_cargo=15000, cargo=0, started=False):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, weight):
        if (weight + self.cargo) <= self.max_cargo:
            self.cargo = weight + self.cargo
        else:
            raise exceptions.CargoOverload()

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp
