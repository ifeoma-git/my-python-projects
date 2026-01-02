"""
COMP.CS.100 Programming 1
Code Template
Author: Ifeoma Nwankwo
"""

def read_message():
    """
    Reads multiple lines of input from the user until an empty line is entered.
    Returns a list of the entered lines (excluding the empty one).
    """
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines


def main():
    """
    Reads a multiline message from the user and prints it in uppercase.
    """
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for line in msg:
        print(line.upper())


if __name__ == "__main__":
    main()
