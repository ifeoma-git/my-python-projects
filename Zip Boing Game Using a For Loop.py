"""
Zip Boing Game Using A For Loop
Author: [Ifeoma Nwankwo]
This program asks the user how many numbers they want to include and prints:
- "zip boing" for numbers divisible by both 3 and 7
- "zip" for numbers divisible by 3
- "boing" for numbers divisible by 7
- The number itself otherwise
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