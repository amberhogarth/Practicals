"""
CP1404 Practical 1 - Menus
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Name: ")
print(MENU)
choice = input(">>>")

while choice != "Q":
    if choice == "H":
        print("Hello {}".format(name))
    elif choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("")
print("Finished.")
