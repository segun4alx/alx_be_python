# multiplication_table.py
# This script prints the multiplication table of a number entered by the user.

# Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
