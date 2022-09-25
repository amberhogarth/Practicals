"""
Amber Hogarth - CP1404 Practical 2 - Determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)
    print_random_score()


def determine_score_status(score):
    """Determine the status for given score"""
    if score < 0 or score > 100:
        return "Invalid score."
    else:
        if 90 <= score <= 100:
            return "Excellent!"
        elif 50 <= score < 90:
            return "Pass."
        else:
            return "Bad."


def print_random_score():
    """Print a random score and its status"""
    random_score = random.randint(0, 101)
    print("Random score: {}".format(random_score))
    random_score_status = determine_score_status(random_score)
    print(random_score_status)


main()
