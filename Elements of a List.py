"""
COMP.CS.100 Programming 1
Reads 5 numbers from the user and prints the ones greater than zero.
Author: Ifeoma Nwankwo
"""

def main():
    print("Give 5 numbers:")
    numbers = []

    for _ in range(5):
        num = int(input("Next number: "))
        numbers.append(num)

    print("The numbers you entered that were greater than zero were:")
    for number in numbers:
        if number > 0:
            print(number)

if __name__ == "__main__":
    main()