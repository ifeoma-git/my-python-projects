"""
COMP.CS.100 Programming 1
A Program that determines whether the numeric value in 'numbers'
are in non-decreasing (ascending) order.

Author: Ifeoma Nwankwo
"""

def is_the_list_in_order(numbers):
    """
    Determines whether the numeric values in `numbers`
    are in non‑decreasing (ascending) order.

    Parameters
    ----------
    numbers : list
        A list of comparable numeric values.

    Returns
    -------
    bool
        True  – if the list is empty, has one element, or each element
                is greater than or equal to the previous one.
        False – if any element is smaller than the one before it.
    """
    # Lists of length 0 or 1 are vacuously in order
    if len(numbers) < 2:
        return True

    # Compare each pair (prev, current)
    prev = numbers[0]
    for current in numbers[1:]:
        if current < prev:
            return False
        prev = current

    return True


# --- quick examples ---
if __name__ == "__main__":
    print(is_the_list_in_order([37, 42, 43]))  # → True
    print(is_the_list_in_order([42, 37, 43]))  # → False
    print(is_the_list_in_order([]))            # → True
    print(is_the_list_in_order([10]))          # → True