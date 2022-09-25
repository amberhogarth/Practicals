"""
CP1404 Practical 1 - Debugging
Broken program to determine score status
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score.")
else:
    if 90 <= score <= 100:
        print("Excellent!")
    elif 50 <= score < 90:
        print("Pass.")
    else:
        print("Bad.")
