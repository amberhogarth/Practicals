"""
Amber Hogarth - CP1404 Practical 3 - Files
"""

# 1
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print(f"Your name is: {name}")

# 3
in_file = open("numbers.txt", 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)

# 4
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
