"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
Author: Ifeoma Nwankwo
"""

from math import sqrt

def area(side1, side2, side3):
    """
    Calculates the area of a triangle using Heron's formula.

    :param side1: Length of the first side of the triangle (float)
    :param side2: Length of the second side of the triangle (float)
    :param side3: Length of the third side of the triangle (float)
    :return: Area of the triangle (float)
    """

    S = (side1 + side2 + side3) / 2
    result = sqrt(S *(S - side1) * (S - side2) * (S - side3))
    return result

def main():

    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    triangle_area = area(a, b, c)
    print(f"The triangle's area is {triangle_area:.1f}")

if __name__ == "__main__":
    main()
