"""
Cheat sheet generator for zip,boing,zip boing
Author: [Ifeoma Nwankwo]
This program ask the user how many numbers they want in the cheat sheet and prints the sequence.
for numbers divisible by 3, it prints 'zip'.
for numbers divisible by 7, it prints 'boing'.
for numbers divisible by both 3 and 7, it prints 'zip boing'.
Otherwise, it prints the number itself.
"""

def main():
    max_number = int(input("How many numbers would you like to have? "))

    for number in range(1, max_number + 1):
        if number %3 == 0 and number %7 == 0:
            print("zip boing")
        elif number %3 == 0:
            print("zip")
        elif number %7 == 0:
            print("boing")
        else:
            print(number)

if __name__ == "__main__":
    main()