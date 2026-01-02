"""
Multiplication Table Until Result Exceeds 100
Author: [Ifeoma Nwankwo]
This program prints the multiplication table for a given number until the result is more than 100.
"""

def main():
    number = int(input("Choose a number: "))
    i = 1

    while i * number <= 100:
        print(f"{i} * {number} = {i * number}")
        i += 1
    #Print the multiplication that exceeds 100
    print(f"{i} * {number} = {i * number}")

if __name__ == "__main__":
    main()
