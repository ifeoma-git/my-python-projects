"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program

Author: Ifeoma Nwankwo
"""

# TODO: add the definition for convert_grades here

def convert_grades(grades):
    """
    Replaces every grade greater than zero in the list `grades`
    with the value 6 (meaning “pass”).

    Parameters
    ----------
    grades : list[int]
        A list of integers (0–5) representing unmodified grades.

    The function works in‑place:
    it modifies the list it receives and returns None.
    It neither prints nor reads any input.
    """
    for i, value in enumerate(grades):
        if value > 0:
            grades[i] = 6

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
