"""
CP1404 Practical 1 - Loops
"""

# Odd numbers.txt from 1 to 20
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# Print n stars
star_amount = int(input("Number of stars: "))
for i in range(star_amount):
    print("*", end=" ")
print()

# Print n lines of increasing stars
star_amount = int(input("Number of stars: "))
for i in range(1, star_amount + 1):
    print("*" * i)
print()
