"""
CP1404 Prac 9 - Unreliable Car Test
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test Cars of different reliabilities."""
    reliable_car = UnreliableCar("reliable car", 100, 100)
    medium_reliable_car = UnreliableCar("medium reliable car", 100, 50)
    unreliable_car = UnreliableCar("unreliable car", 100, 10)

    # drive all cars 20km to see odometer outputs
    reliable_car.drive(20)
    print(reliable_car)
    medium_reliable_car.drive(20)
    print(medium_reliable_car)
    unreliable_car.drive(20)
    print(unreliable_car)


main()
