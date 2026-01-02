"""
COMP.CS.100 Programming 1
A Program that uses function to compare whether list members have an equal value.
Author: Ifeoma Nwankwo
"""

def are_all_members_same(items):
    """
    Returns True if every element in the list `items` is identical,
    or if the list is empty. Otherwise returns False.

    Parameters
    ----------
    items : list
        A list of elements to be compared.

    Returns
    -------
    bool
        True  – all elements are the same (or list is empty)
        False – at least two elements differ
    """
    if not items:          # Empty list → vacuously all the same
        return True
    first = items[0]
    for element in items:
        if element != first:
            return False
    return True


# --- quick examples ---
if __name__ == "__main__":
    print(are_all_members_same([42, 42, 42, 43, 42]))  # → False
    print(are_all_members_same([42, 42, 42, 42]))      # → True
    print(are_all_members_same([]))                    # → True