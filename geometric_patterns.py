"""
COMP.CS.100 Programming 1
Code template for geometric patterns.'
Author: Ifeoma Nwankwo
"""

from math import pi

def get_positive_float(prompt):
    """
    Prompt the user repeatedly until a positive float is entered.

    Parameters:
        prompt (str): The message shown to the user for input.

    Returns:
        float: A positive floating point number input by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass  # ignore non-numeric input and ask again

def calculate_square(side):
    """
    Calculate circumference and area of a square.

    Parameters:
        side (float): Length of one side of the square.

    Returns:
        tuple: (circumference, area) of the square.
    """
    circumference = 4 * side
    area = side * side
    return circumference, area

def calculate_rectangle(side1, side2):
    """
    Calculate circumference and area of a rectangle.

    Parameters:
        side1 (float): Length of the first side.
        side2 (float): Length of the second side.

    Returns:
        tuple: (circumference, area) of the rectangle.
    """
    circumference = 2 * (side1 + side2)
    area = side1 * side2
    return circumference, area

def calculate_circle(radius):
    """
    Calculate circumference and area of a circle.

    Parameters:
        radius (float): Radius of the circle.

    Returns:
        tuple: (circumference, area) of the circle.
    """
    circumference = 2 * pi * radius
    area = pi * radius * radius
    return circumference, area

def square():
    """
    Ask user for square side length, calculate and print circumference and area.
    """
    side = get_positive_float("Enter the length of the square's side: ")
    circumference, area = calculate_square(side)
    print(f"The circumference is {circumference:.2f}")
    print(f"The surface area is {area:.2f}")

def rectangle():
    """
    Ask user for rectangle side lengths, calculate and print circumference and area.
    """
    side1 = get_positive_float("Enter the length of the rectangle's side 1: ")
    side2 = get_positive_float("Enter the length of the rectangle's side 2: ")
    circumference, area = calculate_rectangle(side1, side2)
    print(f"The circumference is {circumference:.2f}")
    print(f"The surface area is {area:.2f}")

def circle():
    """
    Ask user for circle radius, calculate and print circumference and area.
    """
    radius = get_positive_float("Enter the circle's radius: ")
    circumference, area = calculate_circle(radius)
    print(f"The circumference is {circumference:.2f}")
    print(f"The surface area is {area:.2f}")

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ").lower()

        if answer == "s":
            square()

        elif answer == "r":
            rectangle()

        elif answer == "c":
            circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
