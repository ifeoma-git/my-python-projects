"""
COMP.CS.100 Programming 1
A Program that counts how many times the substring 'abba' appears in the given string
Author: Ifeoma Nwankwo
"""

def count_abbas(text):
    """
    Counts how many times the substring 'abba' appears in the given string,
    including overlapping occurrences.

    Args:
        text (str): The string to search in.

    Returns:
        int: The number of times 'abba' appears in the string.
    """
    count = 0
    substring = "abba"
    length = len(substring)

    # If text is shorter than substring, no occurrences possible
    if len(text) < length:
        return 0

    # Check every possible starting index
    for i in range(len(text) - length + 1):
        if text[i:i + length] == substring:
            count += 1

    return count