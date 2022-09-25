"""
Program to print a score menu
"""


def main():
    score = int(input("Score: "))
    get_valid_score(score)


def get_valid_score(score):
    while score < 0 or score > 100:
        return "Invalid score!"



main()