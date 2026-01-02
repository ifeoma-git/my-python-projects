"""
COMP.CS.100 Programming 1
Fully Justified Text Formatter
Author: Ifeoma Nwankwo
"""

def read_input():
    """
    Reads multiline input from the user until an empty line is entered.
    Returns:
        str: A single string containing all the words.
    """
    print("Enter text rows. Quit by entering an empty row.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.strip())
    return " ".join(lines).split()


def format_line(words, max_width):
    """
    Formats a single line of words into fully justified text.

    Args:
        words (list of str): Words to be included in the line.
        max_width (int): Desired character width of the line.

    Returns:
        str: Fully justified line.
    """
    if len(words) == 1:
        return words[0]  # Single word, no extra spaces

    total_chars = sum(len(word) for word in words)
    total_spaces = max_width - total_chars
    space_slots = len(words) - 1

    base_spaces = total_spaces // space_slots
    extra_spaces = total_spaces % space_slots

    justified_line = ""
    for i in range(space_slots):
        justified_line += words[i]
        justified_line += " " * (base_spaces + (1 if i < extra_spaces else 0))
    justified_line += words[-1]  # Add the last word
    return justified_line


def justify_text(words, max_width):
    """
    Justifies a list of words into fully justified lines.

    Args:
        words (list of str): All words from the input text.
        max_width (int): Desired width for each line.

    Returns:
        list of str: List of justified lines.
    """
    result = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > max_width:
            result.append(format_line(current_line, max_width))
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)

    # Last line: left-aligned (no extra spacing)
    if current_line:
        result.append(" ".join(current_line))

    return result


def main():
    """
    Main function to execute the program.
    """
    words = read_input()

    width_input = input("Enter the number of characters per line: ")
    while not width_input.isdigit():
        width_input = input("Please enter a valid number: ")
    max_width = int(width_input)

    justified_lines = justify_text(words, max_width)

    for line in justified_lines:
        print(line)


if __name__ == "__main__":
    main()