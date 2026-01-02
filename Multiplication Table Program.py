"""
Multiplication Table Program
Author: [Ifeoma Nwankwo]
This program prints the multiplication table from 1 to 10 for a number entered by the user.
"""

def main():
    number = int(input("Choose a number: "))

    for i in range(1, 11):
        print(f"{i} * {number} = {i * number}")

if __name__ == "__main__":
    main()