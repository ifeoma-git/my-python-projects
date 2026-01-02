"""
COMP.CS.100 Programming 1
A program that reads a user message in the usual style,
ending with an empty line, and then saves it to a file
so that the file also contains line numbers.
Author: Ifeoma Nwankwo
"""

def read_message():
    """
    Reads multiple lines of user input until an empty line is entered.

    Returns:
        list: A list of input lines.
    """
    print("Enter rows of text. Quit by entering an empty row.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines


def main():
    filename = input("Enter the name of the file: ")

    try:
        # Try opening the file for writing first
        with open(filename, "w") as file:
            lines = read_message()
            for i, line in enumerate(lines, start=1):
                file.write(f"{i} {line}\n")
        print(f"File {filename} has been written.")

    except OSError:
        print(f"Writing the file {filename} was not successful.")


if __name__ == "__main__":
    main()