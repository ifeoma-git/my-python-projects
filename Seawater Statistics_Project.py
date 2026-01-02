"""
COMP.CS.100 Programming 1

This program collects seawater level measurements from the user,
calculates key statistical values (minimum, maximum, median, mean,
standard deviation), and prints them in formatted output.

Author: Ifeoma Nwankwo
Date: 16/07/2025
"""

import math


def read_measurements():
    """
    Reads seawater level measurements from user input until an empty line is entered.

    Returns:
        list of float: List of entered measurements.
    """
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    measurements = []
    while True:
        line = input()
        if line == "":
            break
        try:
            value = float(line)
            measurements.append(value)
        except ValueError:
            print("Invalid input. Please enter a number or an empty line to stop.")

    return measurements


def calculate_median(data):
    """
    Calculates the median of a list of numbers.

    Args:
        data (list of float): The list of measurements.

    Returns:
        float: The median value.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def calculate_mean(data):
    """
    Calculates the mean (average) of a list of numbers.

    Args:
        data (list of float): The list of measurements.

    Returns:
        float: The mean value.
    """
    return sum(data) / len(data)


def calculate_std_deviation(data, mean):
    """
    Calculates the standard deviation of a list of numbers.

    Args:
        data (list of float): The list of measurements.
        mean (float): The mean value of the data.

    Returns:
        float: The standard deviation.
    """
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)


def main():
    """
    Main function to execute the program.
    """
    measurements = read_measurements()

    if len(measurements) < 2:
        print("Error: At least two measurements must be entered!")
        return

    minimum = min(measurements)
    maximum = max(measurements)
    median = calculate_median(measurements)
    mean = calculate_mean(measurements)
    std_dev = calculate_std_deviation(measurements, mean)

    print(f"Minimum:   {minimum:.2f} cm")
    print(f"Maximum:   {maximum:.2f} cm")
    print(f"Median:    {median:.2f} cm")
    print(f"Mean:      {mean:.2f} cm")
    print(f"Deviation: {std_dev:.2f} cm")


if __name__ == "__main__":
    main()
