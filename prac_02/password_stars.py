"""
Program to check password length print asterisks
"""


def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    min_length = 4
    while len(password) < min_length:
        print("Invalid length!")
        password = input("Password: ")
    return password


main()
