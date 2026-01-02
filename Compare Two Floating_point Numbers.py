"""
COMP.CS.100 Programming 1
A program that compares two floating-point numbers for near equality.
Author: Ifeoma Nwankwo
"""

def compare_floats(a, b, epsilon):
    """
    compares two floating-point numbers for near-equality.

    Parameters:
       a (float): The first number to compare.
       b (float): The second number to compare.
       epsilon (float): The maximum allowed differences to still consider the numbers equal.

    Returns:
        bool: True if the absolute difference between a and b is less than epsilon, otherwise false.
    """

    return abs(a - b) < epsilon
