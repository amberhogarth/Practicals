"""
Amber Hogarth - CP1404 Practical 2 - Program to print a score menu
"""

VALID_CHOICES = "S", "R", "Q"
MENU = """R - Result
S - Stars
Q - Quit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = get_valid_choice()
    while choice != "Q":
        if choice == "R":
            score_status = display_score_status(score)
            print(score_status)
            print(MENU)
            choice = get_valid_choice()
        elif choice == "S":
            print_stars(score)
            print(MENU)
            choice = get_valid_choice()
    print("Goodbye.")


def get_valid_score():
    """Get a valid score"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid choice!")
        score = int(input("Score: "))
    return score


def display_score_status(score):
    """Display the status of the score"""
    if 90 <= score <= 100:
        return "Excellent!"
    elif 50 <= score < 90:
        return "Pass."
    else:
        return "Bad."


def get_valid_choice():
    """Get a valid menu choice"""
    choice = input(">>> ").upper()
    while choice not in VALID_CHOICES:
        print("Invalid option!")
        print(MENU)
        choice = input(">>> ").upper()
    return choice


def print_stars(score):
    """Print a line of asterisks based on the score"""
    print("*" * score)


main()
