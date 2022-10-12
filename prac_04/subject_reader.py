"""
CP1404 Prac 4 - Amber Hogarth - Subject Reader
"""

FILENAME = "subject_data"


def main():
    data = get_data()
    print(data)
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
        print("----------")
    input_file.close()
    return data


def display_data(data):
    """Display data neatly."""
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]:12} and has {subject_data[2]} students")


main()
