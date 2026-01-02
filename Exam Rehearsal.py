"""
COMP.CS.100 Programming 1
A program that replaces the initial address of a person with s new address.

Author: Ifeoma Nwankwo
"""
def main():
    """
    w - Translates a word
    A - Adds a word
    R - Removes a word
    P - Prints all the dictionary entries alphabetically
    T - Translates a sentence
    Q - Quits the program
    """

    english_spannish = {"hey":"hola","thanks":"gracias","home":"casa"}

    while True:
        command = input("[W]ORD/[A]DD/[R]EMOVE/[P]RINT/[T]RANSLATE/[Q]UIT:").Upper()

        if command == "W":
            word = input("Enter the word to translate to spanish").strip()
            if word in english_spannish:
                print(f"The word {word} in Spanish is {english_spannish[word]}")
            else:
                print(f"The word {word} cannot be found in the dictionary")

        elif command == "A":
            eng_word = input("Enter the word in English: ").strip()
            spa_word = input("Enter the word in Spanish: ").strip()
            english_spannish[eng_word] = spa_word

        elif command == "R":
         word_to_removed = input("Enter the word to remove: ").strip()
        if word_to_removed in english_spannish:
            del english_spannish[word_to_removed]
        else:
            print(f"The word {word_to_removed} cannot be found in the dictionary")

        elif command == "P":
        for word in sorted(english_spannish):
            print(f"{word} {english_spannish[word]}")

        elif command == "T":
        sentence = input("Enter the text to translate to spanish: ").strip()
        translated = []

        for word in sentence.split():
         translated.append(english_spannish.get(word, word))
        print("The translated text is")
        print("".join(translated))

        elif command == "Q":
        print("Adios!")
        break

    else:
        print("Please Enter Your Command (W/A/R/P/T/Q):")

if __name__ =="__main__":
   main()




