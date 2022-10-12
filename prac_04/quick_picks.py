"""
CP1404 Prac 4 - Amber Hogarth - Quick Picks
"""

import random
MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

number_of_quick_picks = int(input("Number of quick picks: "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))
