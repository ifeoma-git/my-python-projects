"""
COMP.CS.100 Programming 1
A program that checks whether the file exists
and can be read.
Author: Ifeoma Nwankwo
"""

def main():
    filename = input("Enter the name of the file: ")

    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                print(f"{line_number} {line.rstrip()}")
                line_number += 1
    except OSError:
        print("There was an error in reading the file.")


if __name__ == "__main__":
    main()