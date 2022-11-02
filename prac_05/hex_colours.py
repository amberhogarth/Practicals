"""
CP1404 Prac 5 - Amber Hogarth - Hex Colours
"""

COLOUR_TO_CODE = {"amber": "ffbf00", "baby blue": "89cff0", "camel": "c19a6b", "deep space sparkle": "4a646c",
                  "eggshell": "f0ead6", "frostbite": "e936a7", "ginger": "b06500", "honolulu blue": "006db0",
                  "iris": "5a4fcf", "jasmine": "f8de7e"}

print(COLOUR_TO_CODE)
colour = input("Colour: ").lower()
while colour != "":
    try:
        print(f"The colour {colour} has a code of {COLOUR_TO_CODE[colour]}")
        colour = input("Colour: ").lower()
    except KeyError:
        print("That is not a valid colour!")
        colour = input("Colour: ").lower()
