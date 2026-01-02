"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""

class Character:
    def __init__(self, name, hp=10):
        self.__name = name
        self.__hp = hp
        self.__inventory = {}

    def get_name(self):
        return self.__name

    def give_item(self, item):
        self.__inventory[item] = self.__inventory.get(item, 0) + 1

    def remove_item(self, item):
        if item in self.__inventory:
            self.__inventory[item] -= 1
            if self.__inventory[item] <= 0:
                del self.__inventory[item]

    def has_item(self, item):
        return item in self.__inventory

    def how_many(self, item):
        return self.__inventory.get(item, 0)

    def printout(self):
        print(f"Name: {self.__name}")
        print(f"Hitpoints: {self.__hp}")
        for item in sorted(self.__inventory):
            print(f"  {self.__inventory[item]} {item}")

    def pass_item(self, item, target):
        if self.has_item(item):
            target.give_item(item)
            self.remove_item(item)
            return True
        return False

    def attack(self, target, weapon):
        if weapon not in WEAPONS:
            print(f'Attack fails: unknown weapon "{weapon}".')
            return False
        if self is target:
            print(f"Attack fails: {self.__name} can't attack him/herself.")
            return False
        if not self.has_item(weapon):
            print(f'Attack fails: {self.__name} doesn\'t have "{weapon}".')
            return False

        damage = WEAPONS[weapon]
        target.__hp -= damage
        print(f"{self.__name} attacks {target.__name} delivering {damage} damage.")

        if target.__hp <= 0:
            print(f"{self.__name} successfully defeats {target.__name}.")

        return True


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
