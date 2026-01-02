"""
COMP.CS.100 Programming 1

A Program that encrypts a single character using ROT-13 encryption.

Author: Ifeoma Nwankwo
"""

def encrypt(char: str) -> str:
    """
    Encrypt a single character using ROT-13 encryption.

    Parameters:
    char (str): A single character to encrypt.

    Returns:
    str: The ROT-13 encrypted character. Non-alphabetical characters are returned unchanged.

    Examples:
    >>> encrypt("e")
    'r'
    >>> encrypt("E")
    'R'
    >>> encrypt("?")
    '?'
    """
    REGULAR_CHARS = list("abcdefghijklmnopqrstuvwxyz")
    ENCRYPTED_CHARS = list("nopqrstuvwxyzabcdefghijklm")

    # Check if character is lowercase letter
    if char.islower():
        if char in REGULAR_CHARS:
            index = REGULAR_CHARS.index(char)
            return ENCRYPTED_CHARS[index]
        else:
            return char

    # Check if character is uppercase letter
    elif char.isupper():
        lower_char = char.lower()
        if lower_char in REGULAR_CHARS:
            index = REGULAR_CHARS.index(lower_char)
            # Convert the encrypted char back to uppercase
            return ENCRYPTED_CHARS[index].upper()
        else:
            return char

    # Return the character unchanged if not alphabetic
    else:
        return char


def row_encryption(text: str) -> str:
    """
    Encrypt an entire string using ROT-13 encryption by encrypting each character.

    Parameters:
    text (str): The input string to encrypt.

    Returns:
    str: The ROT-13 encrypted string.

    Examples:
    >>> row_encryption("Happy, happy, joy, joy!")
    'Unccl, unccl, wbl, wbl!'
    >>> row_encryption("")
    ''
    """
    encrypted_text = ""
    for c in text:
        encrypted_text += encrypt(c)
    return encrypted_text