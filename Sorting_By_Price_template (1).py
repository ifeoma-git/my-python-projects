"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 152577546
Name: Ifeoma Nwankwo
Email: ifeoma.nwankwo@tuni.fi

Template for sorting by price assignment.
"""

"""
Price list assignment: Print items sorted by price in increasing order.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15, "pizza": 4.15,
}


def main():
    # Sort items by value (price) using sorted() and lambda
    sorted_items = sorted(PRICES.items(), key=lambda item: item[1])

    # Print each product and its price formatted to two decimal places
    for product, price in sorted_items:
        print(f"{product} {price:.2f}")


if __name__ == "__main__":
    main()
