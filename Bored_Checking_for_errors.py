"""
Author: [Ifeoma Nwankwo]
This program repeatedly asks the user to answer `Y` or `N`.
It only accepts `y`,`Y`,`n`,`N` as valid answers.
If the user enters anything else, the program asks again.
"""

def main():
    while True:
        answer = input("Answer Y or N: ")
        if answer in ("y", "Y", "n", "N"):
            print(f"You answered {answer}")
            break
        else:
            print("Incorrect entry. ")

if __name__ == "__main__":
    main()
