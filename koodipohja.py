"""
COMP.CS.100 Programming 1
Assignment "Improved Box Printing" code template
Author: Ifeoma Nwankwo
"""

def print_box(width: int,
              height: int,
              border_mark: str = "#",
              inner_mark: str = " ") -> None:
    """
    Print a hollow rectangle (box) of the given width and height.

    Parameters
    ----------
    width : int
        The number of characters on each line (≥ 2 for a hollow box).
    height : int
        The number of lines in the box (≥ 2 for a hollow box).
    border_mark : str, optional
        The character used for the border; defaults to "#".
    inner_mark : str, optional
        The character used for the inside of the box; defaults to " ".
    """
    if width < 2 or height < 2:
        # Not enough space for a hollow box; nothing is printed.
        return

    # Top border
    print(border_mark * width)

    # Middle rows: border_mark + inner area + border_mark
    for _ in range(height - 2):
        print(border_mark + inner_mark * (width - 2) + border_mark)

    # Bottom border
    print(border_mark * width)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
