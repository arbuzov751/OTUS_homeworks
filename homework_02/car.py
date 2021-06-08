"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = Engine(int, int)

    def set_engine(self, engine: Engine):
        self.engine = engine
