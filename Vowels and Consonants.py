"""
COMP.CS.100 Programming 1
 A Program that counts the number of vowels and consonants in a given English word.

 Author: Ifeoma Nwankwo
"""

def count_vowels_and_consonants(word):
    """
    Counts the number of vowels and consonants in a given English word.
    Treats 'y' as a vowel.

    Parameters:
        word (str): The input word consisting of lowercase letters only.

    Returns:
        tuple: A tuple containing the number of vowels and consonants (vowel_count, consonant_count).
    """
    vowels = "aeiouy"
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count, consonant_count


# Main program
def main():
    word = input("Enter a word: ")
    vowel_count, consonant_count = count_vowels_and_consonants(word)
    print(f'The word "{word}" contains {vowel_count} vowels and {consonant_count} consonants.')

# Run the program
if __name__ == "__main__":
    main()