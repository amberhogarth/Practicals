"""
CP1404 Practical 7 - More Guitars!
Estimated time: 30 mins
Actual time: 35 mins
"""

from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", "r")

    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), parts[2])
        guitars.append(guitar)
    in_file.close()

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        print(new_guitar, "added.")
        guitars.append(new_guitar)
        name = input("Name: ")
    guitars.sort()

    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file, end="\n")
    out_file.close()


main()
