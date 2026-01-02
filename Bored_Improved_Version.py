"""
Asks the user repeatedly if they are bored until they reply with 'y' or 'Y'.
Only accepts 'y','Y','n' or 'N' as valid inputs. Prints an error message otherwise.

Author: [Ifeoma Nwankwo]
"""

def main():
    while True:
        user_input = "" #Initialize before inner loop

        #Inner loop: ensure input is valid
        while user_input not in["y","Y","n","N"]:
            user_input = input("Bored? (y/n) ")
            if user_input not in["y","Y","n","N"]:
                print("Incorrect entry.")

        #if the user is bored, break the outer loop
        if user_input in["y","Y"]:
            print("Well, let's stop this, then.")
            break

if __name__ == "__main__":
    main()