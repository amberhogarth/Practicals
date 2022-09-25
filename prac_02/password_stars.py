"""
Program to check password length print asterisks
"""


def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    """Prints a line of asterisks based on the length of the password"""
    print("*" * len(password))


def get_password():
    """Gets password input and verifies it meets length requirements"""
    password = input("Password: ")
    min_length = 4
    while len(password) < min_length:
        print("Invalid length!")
        password = input("Password: ")
    return password


main()
