""""""

from prac_07.guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), parts[2])
        guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
