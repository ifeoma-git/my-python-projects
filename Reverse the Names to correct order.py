"""
COMP.CS.100 Programming 1

A Program that converts a name string from 'Last, First' format to 'First Last' format.

Author: Ifeoma Nwankwo
"""

def reverse_name(name):
    """
    Takes a name string that may be in 'Last, First' format and returns it in 'First Last' format.
    The function removes any unnecessary spaces and handles edge cases like missing first or last names.

    Parameters:
    name (str): A name string possibly containing a comma.

    Returns:
    str: The name in 'First Last' format or as-is if no comma is present.
    """
    name = name.strip()

    if ',' not in name:
        return name

    parts = name.split(',')
    if len(parts) != 2:
        return name.strip()

    last = parts[0].strip()
    first = parts[1].strip()

    if not first:
        return last
    elif not last:
        return first
    else:
        return f"{first} {last}"


# Test the function
if __name__ == "__main__":
    test_cases = [
        "Techie, Teddy",
        "Scumble,    Arnold",
        "Fortunato,Frank",
        "von Grünbaumberger, Herbert",
        "   Duck,     Donald  ",
        "X,",
        ",X",
        " , Y ",
        ",",
        "Stuart Student",
        "Mando"
    ]

    for case in test_cases:
        print(f'Input: "{case}" → Output: "{reverse_name(case)}"')