"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. A ValueError will occur when the numerator or denominator input is not a
# valid integer (for example, the user entered a letter or a float)
# 2. A ZeroDivisionError will occur when the denominator input is "0". A general rule
# of division is that any value divided by zero is undefined; as such, the program will not
# be able to carry out the division.
# 3. To avoid a ZeroDivisionError, a while loop could be added to ask the user for a new denominator if 0 is entered.
