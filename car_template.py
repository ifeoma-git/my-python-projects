"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
Author: Ifeoma Nwankwo
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    gas_after_fill = gas + to_fill
    if gas_after_fill > tank_size:
        gas_after_fill = tank_size
    return gas_after_fill


def drive(x1, y1, x2, y2, gas, consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """

    dist = distance(x1, y1, x2, y2)
    needed = gas_needed(dist, consumption)

    if needed <= gas:
        # Enough gas to reach destination
        gas -= needed
        return gas, x2, y2
    else:
        # Not enough gas to reach destination
        max_dist = (gas / consumption) * 100
        ratio = max_dist / dist
        new_x = x1 + (x2 - x1) * ratio
        new_y = y1 + (y2 - y1) * ratio
        gas = 0  # Used all gas
        return gas, new_x, new_y


def distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean distance between two points (x1, y1) and (x2, y2).
    Returns the distance as a float.
    """
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def gas_needed(distance, consumption):
    """
    Calculates the amount of gas needed to drive the given distance.
    Consumption is gas liters per 100 km.
    Returns the amount of gas needed as a float.
    """
    return (distance * consumption) / 100


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
