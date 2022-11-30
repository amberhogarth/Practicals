"""
CP1404 Prac 9 - Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
VALID_CHOICES = "qcd"


def main():
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    chosen_taxi = None
    print(MENU)
    choice = input(">>> ").lower()
    while choice not in VALID_CHOICES:
        print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                chosen_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if chosen_taxi:
                chosen_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                chosen_taxi.drive(drive_distance)
                trip_cost = chosen_taxi.get_fare()
                print(f"Your {chosen_taxi.name} trip cost you ${trip_cost:.2f}")
                bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display organised list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
