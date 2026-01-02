"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
Author: Ifeoma Nwankwo
"""

def print_verse(animal,sound):
    """
    Prints the verse of "Old MacDonald Had a Farm"
    song for a given animal and its sound.

    Parameters:
       animal (str): The name of the animal.
       sound (str): The sound that the animal makes.

    Returns:
        None
    """

    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {sound} {sound} here")
    print(f"And a {sound} {sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound} {sound}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def main():
    animals = [
        ("cow","moo"),
        ("pig","oink"),
        ("duck","quack"),
        ("horse","neigh"),
        ("lamb","baa")
    ]

    for i in range(len(animals)):
        animal,sound = animals[i]
        print_verse(animal,sound)
        #Print empty line only if it's not the last verse
        if i < len(animals) - 1:
            print()

if __name__ == "__main__":
    main()
