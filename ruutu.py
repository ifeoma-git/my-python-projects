"""
COMP.CS.100 Programming 1
Template for task: box printing
Author: Ifeoma Nwankwo
"""
def print_box(w, h, ch):
    """
    Prints a rectangular box using the specified character.

    Parameters:
        w (str): The width of the box (should be convertible to int).
        h (str): The height of the box (should be convertible to int).
        ch (str): The character used to draw the box.

    The function converts the width and height to integers and prints a box of height
    'h' where each line contains 'w' characters of 'ch'
    """
    for _ in range(int(h)):
        print(ch * int(w))

def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
