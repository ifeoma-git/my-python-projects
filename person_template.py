"""
COMP.CS.100 Programming
A program that shows The first example of a home-made
class with extended functionality.

Author: Ifeoma Nwankwo
"""

class Person:
    """
    This class models a person with a simple electronic wallet and address.
    """

    def __init__(self, name, initial_money, address):
        """
        A person object is initialized with the name,
        initial amount of money in the wallet, and address.

        :param name: str, the name of the person whose
            spending the object is following.
        :param initial_money: float, how much money will
            there be in the wallet at the point of creation.
        :param address: str, the person's initial address.
        """
        self.__name = name
        self.__money = initial_money
        self.__address = address

    def move(self, new_address):
        """
        Changes the person's address.

        :param new_address: str, the new address where the person moved.
        """
        self.__address = new_address

    def printout(self):
        """
        Prints a formatted summary of the person's information:
        name, wealth, and address.
        """
        print("—" * 25)
        print("Name:   ", self.__name)
        print("Wealth: ", self.__money)
        print("Address: ", self.__address)

    def add_money(self, amount):
        """
        Adds money to the electronic wallet.

        :param amount: float, the amount of money added.
        :return: True if operation successful, False otherwise.
        """
        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True

    def make_payment(self, price):
        """
        Deducts money from the person's wallet if affordable.

        :param price: float, the price of the purchase
        """
        if price < 0.0:
            print("The price can't be negative.")
        elif price > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= price


def main():
    # Let's create an object of type Person, name it denzil,
    # and use it to spy on Prof. Dexter's spending.
    denzil = Person("Denzil Dexter", 100.00, "320 Memorial Dr.")

    # State of Denzil before moving
    denzil.printout()

    # Denzil moves out of a dormitory to a place of his own.
    denzil.move("20 Chestnut St.")

    # Where's Denzil after the move.
    denzil.printout()


if __name__ == "__main__":
    main()
