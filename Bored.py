"""
Author: [Ifeoma Nwankwo]
This program repeatedly asks the user if they are bored.
When the user answers 'y', the program stops and prints a final message
"""

def main():
    answer = ""
    while answer != "y":
        answer = input("Bored? (y/n) ")

    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()