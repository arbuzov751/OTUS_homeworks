from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 1200
    started = False
    fuel = 0
    fuel_consumption = 7

    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError(Exception)

    def move(self, distance):
        if (self.fuel - distance * self.fuel_consumption) > 0:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel(Exception)
