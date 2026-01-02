"""
This program asks the user for  their name and greets them with a formatted message.
The greeting ensures the comma is attached directly to the user's name without an extra space.

Author: [Ifeoma Nwankwo]
"""

def main():
    name = input("Tell us your name: ")
    print("Hey",name + ",","the printout formatting is going well!")

if __name__ == "__main__":
    main()