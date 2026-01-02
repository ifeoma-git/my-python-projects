"""
COMP.CS.100 Programming 1
A program that repeatedly prompts the user for input until a valid positive integer is entered.
Author: Ifeoma Nwankwo
"""

def read_input(prompt):
    """
    Repeatedly prompts the user for input until a valid positive integer is entered.

    Parameters:
        prompt (str): The input prompt to show the user.

    Returns:
        int: A positive integer entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value > 0:
                return value
        except ValueError:
            continue  # Do nothing, just re-prompt


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()  # <-- Print the empty line before the frame

    for _ in range(height):
        print(mark * width)


if __name__ == "__main__":
    main()