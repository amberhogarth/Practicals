"""
CP1404 Prac 5 - Amber Hogarth - Emails
Estimated: 25 minutes
Actual: 35 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? Y/n ").upper()
        if name_confirmation != "Y" and name_confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Get name from email address."""
    prefix = email.split("@")[0]
    prefix_parts = prefix.split(".")
    name = " ".join(prefix_parts).title()
    return name


main()
