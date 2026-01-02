def calculate_change(purchase_price, paid_amount):
    """Calculates the change breakdown using 10,5,2,and 1 euro denominations.

    Parameters:
    purchase_price(int): The cost of the purchase.
    paid_amount(int): The amount paid by the customer.

    Returns:
    dict: Denominations and their respective counts.
    """

    change = paid_amount - purchase_price
    denominations = [10,5,2,1]
    change_breakdown = {}

    for denom in denominations:
        count = change // denom
        if count:
            change_breakdown[denom] = count
        change %= denom

    return change_breakdown

def main():
    number_words = {
        10: "ten",
        5: "five",
        2: "two",
        1: "one"
    }
    purchase_price = int(input("Purchase price: "))
    paid_amount = int(input("Paid amount of money: "))

    if paid_amount < purchase_price:
       print("Paid amount is less than the purchase price.")
       return

    print("Offer change:")
    change = calculate_change(purchase_price, paid_amount)

    for denom in [10,5,2,1]: #Maintain order
        if denom in change:
           if denom >= 5:
              print(f"{change[denom]} {number_words[denom]} - euro notes")

        else:
            print(f"{change[denom]} {number_words[denom]} - euro coins")

main()