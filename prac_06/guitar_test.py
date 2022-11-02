"""CP1404/CP5632 Practical - Guitars! Testing"""

from prac_06.guitar import Guitar


def main():
    """Test Guitar class with various function outputs."""
    # Test __str__()
    initial_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(initial_guitar)

    another_guitar = Guitar("Another Guitar", 2013)  # No price (=$0.00)
    print(another_guitar)

    # Test get_age() and is_vintage()
    print(f"{initial_guitar.name} get_age() - Expected 100. Got {initial_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
    print(f"{initial_guitar.name} is_vintage() - Expected True. Got {initial_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == '__main__':
    main()
