"""
COMP.CS.100 Programming 1

A Program that creats an acronym from the given name.

Author: Ifeoma Nwankwo
"""

def create_an_acronym(name):
    """
    Create an acronym from the given name.

    This function takes a string as input and returns its acronym.
    An acronym is formed by taking the first letter of each word in the name,
    capitalizing it, and concatenating the letters.

    Parameters:
    name (str): The name or phrase from which to create an acronym.
                It is assumed to contain at least one character.

    Returns:
    str: The acronym formed from the input string.

    Example:
    >>> create_an_acronym("central intelligence agency")
    'CIA'
    """
    words = name.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

# Example usage:
if __name__ == "__main__":
    user_input = input("Enter a name or phrase: ")
    print(f"Acronym: {create_an_acronym(user_input)}")