"""
Amber Hogarth - CP1404 Practical 2 - Temperature conversion
"""

VALID_CHOICES = "C", "F", "Q"
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = get_valid_choice()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = convert_to_celsius()
            print("Result: {:.2f} C".format(celsius))
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_choice():
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICES:
        print("Invalid option!")
        print(MENU)
        choice = input(">>> ").upper()
    return choice


def convert_to_celsius():
    """Convert temperature from fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit():
    """Convert temperature from celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
