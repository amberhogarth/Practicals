"""
Program to check password length print asterisks
"""
password = input("Password: ")
min_length = 4

while len(password) < min_length:
    print("Invalid length!")
    password = input("Password: ")

print("*" * len(password))
