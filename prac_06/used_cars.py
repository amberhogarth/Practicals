"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("i30", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    test_car = Car("limo", 100)
    test_car.add_fuel(20)
    print(f"{test_car.name} has fuel: {test_car.fuel}")
    test_car.drive(115)
    print(test_car)



main()
