"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
Author: Ifeoma Nwankwo
"""

import math

def calculate_angle(*angles):
    """
    Calculates the third angle of a triangle based on the number of given angles.
    - If one angle is given, assumes it's part of a right-angled triangle and returns the other sharp angle.
    - If two angles are given, returns the third angle by subtracting the sum from 180.

    :param angles: One or two angles as positional arguments.
    :return: The missing angle as an integer.
    """
    if len(angles) == 1:
        return 90 - angles[0]
    elif len(angles) == 2:
        return 180 - angles[0] - angles[1]

def read_positive_float(prompt):
    """
    Prompts the user with a message until a positive float is entered.

    :param prompt: The prompt string to show the user.
    :return: A positive float value.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass  # If not a float, ignore and re-prompt.
        # Re-prompt with the same message if input is invalid or non-positive.

def calculate_square(side):
    """
    Calculates the circumference and area of a square.

    :param side: The length of the square's side.
    :return: A tuple containing (circumference, area).
    """
    circumference = 4 * side
    area = side * side
    return circumference, area

def calculate_rectangle(side1, side2):
    """
    Calculates the circumference and area of a rectangle.

    :param side1: Length of first side.
    :param side2: Length of second side.
    :return: A tuple containing (circumference, area).
    """
    circumference = 2 * (side1 + side2)
    area = side1 * side2
    return circumference, area

def calculate_circle(radius):
    """
    Calculates the circumference and area of a circle.

    :param radius: The radius of the circle.
    :return: A tuple containing (circumference, area).
    """
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

def print_results(circumference, area):
    """
    Prints the circumference and area formatted to two decimal places.

    :param circumference: The circumference to print.
    :param area: The area to print.
    """
    print(f"The circumference is {circumference:.2f}")
    print(f"The surface area is {area:.2f}")

def menu():
    """
    Displays the menu for user to select geometric pattern and performs corresponding actions.
    Loops until the user chooses to quit.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            side = read_positive_float("Enter the length of the square's side: ")
            circ, area = calculate_square(side)
            print_results(circ, area)

        elif answer == "r":
            side1 = read_positive_float("Enter the length of the rectangle's side 1: ")
            side2 = read_positive_float("Enter the length of the rectangle's side 2: ")
            circ, area = calculate_rectangle(side1, side2)
            print_results(circ, area)

        elif answer == "c":
            radius = read_positive_float("Enter the circle's radius: ")
            circ, area = calculate_circle(radius)
            print_results(circ, area)

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # empty line for readability

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()

