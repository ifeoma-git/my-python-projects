def calculate_change(purchase_price, paid_amount):
    """
    Calculates the change in terms of 10,5,2, and 1 euro notes and coins.

    Parameters:
    purchase_price(int): The cost of the purchase.
    paid_amount(int): The amount of money provided.

    Returns:
    dict or str: The number of each denomination to return as change or as a message.
    """

    change = paid_amount - purchase_price
    change_breakdown = {}

    if change == 0:
        return "No change"
    elif change < 0:
        return "No change"

    denominations = [
        (10,'ten-euro notes'),
        (5,'five-euro notes'),
        (2,'two-euro coins'),
        (1,'one-euro coins')
    ]

    for value, name in denominations:
        count = change // value
        if count:
            change_breakdown[name] = count
            change %= value
    return change_breakdown
def main():
    purchase_price = int(input("Purchase price: "))
    paid_amount = int(input("Paid amount of money: "))
    result = calculate_change(purchase_price,paid_amount)

    if isinstance(result,str):
        print(result)
    else:
        print("Offer change:")
        for name,count in result.items():
            print(f"{count} {name}")

if __name__ == "__main__":
   main()

