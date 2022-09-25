"""
Amber Hogarth - CP1404 Practical 3 - Random Numbers
"""

# On line 1, I saw a random integer being picked from a range between 5 and 20. The smallest number I could have
# seen is 5, and the largest was 19.
# On line 2, I saw a random integer (5) being picked from a range between 3 and 10, with the incrementation of 2.
# From smallest to largest, the numbers I could have seen were 3, 5, 7 or 9.
# On line 2, I saw a random float value (5.314...) being picked from a range between 2.5 and 5.5 inclusive.
# The smallest number I could have seen was 2.5 and the largest was 5.5.

# Produce a random number between 1 and 100 inclusive
import random
random_number = random.randint(1, 101)
print(f"Random number: {random_number}")
