def main():

    purchase_price = int(input("Enter the purchase price: "))
    paid_amount = int(input("Enter the paid amount: "))

    if paid_amount == purchase_price:
        print("No Change")
        return

    elif paid_amount < purchase_price:
        print("No money paid")
        return

    change = paid_amount - purchase_price
    print(f"change: {change} euros")

    if change >= 10:
        tens = change // 10
        print(f"{tens} ten-euro-notes")
        change = change % 10

    if change >= 5:
        fives = change // 5
        print(f"{fives} five-euro-notes")
        change = change % 5

    if change >= 2:
        twos = change // 2
        print(f"{twos} two-euro-coins")
        change = change % 2

    if change >= 1:
        ones = change // 1
        print(f"{ones} one-euro-coins")

main()