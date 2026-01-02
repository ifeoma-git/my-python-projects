"""
COMP.CS.100 Programming 1
Print a box with input error checking
Author: Ifeoma Nwankwo
"""

def read_input(prompt):
    """
    Asks the user to enter a positive integer.
    Keeps prompting until the user enters a number > 0
    :param prompt: A string used when asking for input.
    :return: A positive integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass #Ignore non-integer inputs
        #If we get here, the input was invalid or < = 0
        #So we prompt again (loop continues)

def print_box(w, h, m):
    """
    Prints a box of width 'w' and height 'h' using mark 'm'.
    :param w: width of the box
    :param h: Height of the box
    :param m: Character used to print the box
    """

    for _ in range(h):
        print(m * w)

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print() #required empty line before the box
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
