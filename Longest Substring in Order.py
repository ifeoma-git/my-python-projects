"""
COMP.CS.100 Programming 1
A Program that finds and returns the longest substring of the input string
where the characters are in alphabetical order.
Author: Ifeoma Nwankwo
"""

def longest_substring_in_order(string):
    """
    Finds and returns the longest substring of the input string
    where the characters are in alphabetical order.

    If there are multiple equally long substrings, the first one
    encountered is returned.

    If the input is an empty string or a single character, it is returned as is.

    Args:
        string (str): The input string to search.

    Returns:
        str: The longest substring in alphabetical order.
    """
    if len(string) <= 1:
        return string

    longest = current = string[0]

    for i in range(1, len(string)):
        if string[i] >= string[i - 1]:
            current += string[i]
        else:
            current = string[i]

        if len(current) > len(longest):
            longest = current

    return longest