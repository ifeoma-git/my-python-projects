"""
COMP.CS.100 Programming 1
ROT-13 Message Encryption Program
Author: Ifeoma Nwankwo
"""


def read_message():
    """
    Reads multiple lines of input from the user until an empty line is entered.
    Returns:
        list of str: The entered message lines, excluding the empty line.
    """
    message_lines = []
    while True:
        line = input()
        if line == "":
            break
        message_lines.append(line)
    return message_lines


def encrypt(char):
    """
    Encrypts a single character using ROT-13.

    Args:
        char (str): A single character to encrypt.

    Returns:
        str: The encrypted character, or the original character if not a letter.
    """
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        return char


def row_encryption(text):
    """
    Applies ROT-13 encryption to an entire string.

    Args:
        text (str): The input string.

    Returns:
        str: The ROT-13 encrypted version of the string.
    """
    encrypted = ""
    for char in text:
        encrypted += encrypt(char)
    return encrypted


def main():
    """
    Main function to read a multi-line message and print it encrypted using ROT-13.
    """
    print("Enter text rows to the message. Quit by entering an empty row.")
    message = read_message()

    print("ROT13:")
    for line in message:
        print(row_encryption(line))


if __name__ == "__main__":
    main()