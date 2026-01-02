"""
COMP.CS.100 Programming 1
A Program that prints numbers sequentially
Author: Ifeoma Nwankwo
"""

def main():
    """
    Prints all even numbers from 0 to 100 in ascending order,
    and then prints the same even numbers in descending order.
    Each number is printed on its own line.
    """

    # Ascending order: 0 to 100
    for number in range(0, 101, 2):
        print(number)

    # Descending order: 100 to 0
    for number in range(100, -1, -2):
        print(number)


if __name__ == "__main__":
    main()