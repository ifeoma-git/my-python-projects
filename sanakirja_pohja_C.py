"""
COMP.CS.100 Programming 1
A Program that improves the implementation of the printing operation.
Author: Ifeoma Nwankwo
"""

def print_dictionary(english_spanish):
    """
    Prints the contents of the dictionary in both English-Spanish and Spanish-English order.

    Parameters:
        english_spanish (dict): A dictionary where keys are English words and values are Spanish translations.

    Returns:
        None
    """
    print("\nEnglish-Spanish")
    for eng_word in sorted(english_spanish):
        print(f"{eng_word} {english_spanish[eng_word]}")

    # Create the Spanish-English dictionary
    spanish_english = {span: eng for eng, span in english_spanish.items()}

    print("\nSpanish-English")
    for span_word in sorted(spanish_english):
        print(f"{span_word} {spanish_english[span_word]}")
    print()  # Empty line after the dictionary


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    # Initial print of dictionary contents
    print("Dictionary contents:")
    print(", ".join(sorted(english_spanish)))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ").strip()
            if word in english_spanish:
                print(f"in Spanish is {english_spanish[word]}")
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "A":
            eng_word = input("Give the word to be added in English: ").strip()
            span_word = input("Give the word to be added in Spanish: ").strip()
            english_spanish[eng_word] = span_word

            print("Dictionary contents:")
            print(", ".join(sorted(english_spanish)))

        elif command == "R":
            word = input("Give the word to be removed: ").strip()
            if word in english_spanish:
                del english_spanish[word]
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            print_dictionary(english_spanish)

        elif command == "T":
            sentence = input("Enter a sentence to translate: ")
            words = sentence.strip().split()
            translated = [english_spanish.get(word, word) for word in words]
            print(" ".join(translated))

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()