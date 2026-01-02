"""
COMP.CS.100 Programming 1
A program that prints each line of a text file with line number
Author: Ifeoma Nwankwo
"""
def main():
    filename = input("Enter the name of the file: ")
    try:
        # 1. Open the file
        with open(filename, 'r') as file:
            # 2. Read and print each line with line number
            line_number = 1
            for line in file:
                print(f"{line_number} {line.rstrip()}")
                line_number += 1
        # 3. File is automatically closed by 'with' block
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    main()