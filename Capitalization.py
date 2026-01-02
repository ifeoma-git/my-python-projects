"""
COMP.CS.100 Programming 1

A Program that capitalizes the first letter of each word

Author: Ifeoma Nwankwo
"""

def capitalize_initial_letters(text):
    """
    Capitalizes the first letter of each word in the input string and
    converts the remaining letters of each word to lowercase.

    Parameters:
    text (str): A string that may contain one or more words.

    Returns:
    str: The input string with each word capitalized.

    Examples:
    >>> capitalize_initial_letters("drIVING cAR")
    'Driving Car'
    >>> capitalize_initial_letters("")
    ''
    """
    return text.title()