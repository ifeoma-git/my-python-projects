"""
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
Author: Ifeoma Nwankwo
"""

def repeat_name(name, repetitions):
    """
    Prints the name followed by 'Bear', repeated as many times as specified.
    :param name: str, the name to repeat(e.g. "Yogi")
    :param repetitions: int, the number of times to print the name with 'Bear'
    :return: None
    """
    for _ in range(repetitions):
      print(f"{name}, {name} Bear")

def verse(lead_line, name):
    """
    Prints one full verse of the Yogi Bear song using the given lead line and name.
    :param lead_line: str, the opening line of the verse
    :param name: str, the name used in the verse(e.g. "Yogi", "Boo Boo")
    :return: None
    """
    print(lead_line)
    print(f"{name}, {name}")
    print(lead_line)
    print(f"{name}, {name} Bear")
    repeat_name(name, 2)
    print(lead_line)
    print(f"{name}, {name} Bear")

def main():
    """
    Main function that prints three verses of the Yogi Bear song.
    """
    verse("I know someone you don't know","Yogi")
    print()

    verse("Yogi has a best friend too","Boo Boo")
    print()

    verse("Yogi has a sweet girlfriend","Cindy")

if __name__ == "__main__":
   main()
