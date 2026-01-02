"""
COMP.CS.100 Programming 1

A program that add a printout at the start of the tourist dictionary
program to make it easier to use.

Author: Ifeoma Nwankwo
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    # Print initial dictionary contents in alphabetical order
    print("Dictionary contents:")
    print(", ".join(sorted(english_spanish)))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "A":
            eng = input("Give the word to be added in English: ")
            spa = input("Give the word to be added in Spanish: ")
            english_spanish[eng] = spa

            # Print updated dictionary contents
            print("Dictionary contents:")
            print(", ".join(sorted(english_spanish)))

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            words = sentence.split()
            translated = []
            for word in words:
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