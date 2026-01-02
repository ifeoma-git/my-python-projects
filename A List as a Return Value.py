"""
COMP.CS.100 Programming 1
‑ Input‑to‑List & Search

A small program that
1. reads *n* integers into a list (function `input_to_list`)
2. asks what number to search for
3. tells the user how many times that number occurs in the list.

Author: Ifeoma nwankwo
"""


def input_to_list(amount):
    """
    Reads `amount` integers from the user and returns them in a list.

    Parameters
    ----------
    amount : int
        The number of integer values to read.

    Returns
    -------
    list[int]
        A list containing the entered integers in the order given.
    """
    print(f"Enter {amount} numbers:")
    nums = []
    for _ in range(amount):
        nums.append(int(input()))
    return nums


def main():
    how_many = int(input("How many numbers do you want to process: "))
    numbers = input_to_list(how_many)

    target = int(input("Enter the number to be searched: "))
    occurrences = numbers.count(target)

    if occurrences == 0:
        print(f"{target} is not among the numbers you have entered.")
    else:
        print(f"{target} shows up {occurrences} times among the numbers you have entered.")


if __name__ == "__main__":
    main()