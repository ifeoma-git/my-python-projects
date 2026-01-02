"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.

Author: Ifeoma Nwankwo
"""

def main():
    """
    A simple English-Spanish dictionary program that allows the user to:
    - Translate a word (W)
    - Add a new word pair (A)
    - Remove a word (R)
    - Print all dictionary entries alphabetically (P)
    - Translate a sentence (T)
    - Quit the program (Q)
    """
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").upper()

        if command == "W":
            word = input("Enter the word to be translated: ").strip()
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "A":
            eng_word = input("Give the word to be added in English: ").strip()
            spa_word = input("Give the word to be added in Spanish: ").strip()
            english_spanish[eng_word] = spa_word

        elif command == "R":
            word_to_remove = input("Give the word to be removed: ").strip()
            if word_to_remove in english_spanish:
                del english_spanish[word_to_remove]
            else:
                print(f"The word {word_to_remove} could not be found from the dictionary.")

        elif command == "P":
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ").strip()
            translated = []
            for word in sentence.split():
                translated.append(english_spanish.get(word, word))
            print("The text, translated by the dictionary:")
            print(" ".join(translated))

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
