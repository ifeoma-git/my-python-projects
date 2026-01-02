"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Implementation of the product assignment.
Author: Ifeoma Nwankwo
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    Each product has a name, a price, and an optional sale percentage.
    """

    def __init__(self, name, price):
        """
        Initializes the product with its name and original price.
        By default, the product is not on sale (sale percentage = 0.0).
        :param name: str, name of the product
        :param price: float, original price of the product
        """
        self.__name = name
        self.__price = price
        self.__sale_percentage = 0.0

    def set_sale_percentage(self, percentage):
        """
        Sets the product's sale percentage.
        :param percentage: float, sale percentage (e.g., 10.0 means 10%)
        """
        self.__sale_percentage = percentage

    def get_price(self):
        """
        Calculates and returns the current price of the product.
        If a sale percentage is applied, the sale price is returned.
        :return: float, current price after discount if any
        """
        discount = self.__price * (self.__sale_percentage / 100)
        return self.__price - discount

    def printout(self):
        """
        Prints out the product details: name, price, and sale percentage.
        """
        print(f"{self.__name}")
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale_percentage:.2f}")


def main():
    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
