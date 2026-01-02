"""
COMP.CS.100 Programming 1
A Program that Implements a world density calculator.
Author: Ifeoma Nwankwo
"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")

    word_count = {}  # Dictionary to store word frequencies

    while True:
        line = input()
        if line == "":
            break

        # Split line into words, convert to lowercase
        words = line.lower().split()

        for word in words:
            if word in word_count:
                word_count[word] += 1  # Increment count if already exists
            else:
                word_count[word] = 1   # Initialize count for new word

    # Print words and their counts in alphabetical order
    for word in sorted(word_count):
        print(f"{word} : {word_count[word]} times")


if __name__ == "__main__":
    main()