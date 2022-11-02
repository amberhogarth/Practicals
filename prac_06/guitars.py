"""CP1404/CP5632 Practical - Guitars! Program"""

from prac_06.guitar import Guitar


def main():
    print("My Guitars!")
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        print(f"{new_guitar.name} ({new_guitar.year}) : ${new_guitar.cost:,.2f} added.")
        guitars.append(new_guitar)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print(". . . snip . . .")
    print("These are my guitars:")
    guitar_number = 0
    for guitar in guitars:
        guitar_number += 1
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {guitar_number}: {guitar.name:19} ({guitar.year}), worth ${guitar.cost:9.2f}{vintage_string}")


if __name__ == '__main__':
    main()
