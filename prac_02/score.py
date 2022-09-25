"""
CP1404 Practical 1 - Debugging
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    print(determine_score_status(score))
    random_score = random.randint(0, 101)
    print("Random score: {}".format(random_score))
    print(determine_score_status(random_score))


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score."
    else:
        if 90 <= score <= 100:
            return "Excellent!"
        elif 50 <= score < 90:
            return "Pass."
        else:
            return "Bad."


main()
