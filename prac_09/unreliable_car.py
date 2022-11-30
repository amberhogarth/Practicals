"""
CP1404 Prac 9 - Unreliable Car Class
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """A class for an unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car randomly depending on random number and reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        drive_distance = super().drive(distance)
        return drive_distance
