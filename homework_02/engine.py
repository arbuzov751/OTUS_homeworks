"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons

