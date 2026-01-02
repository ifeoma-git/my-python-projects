def main():
    age = int(input("Please, enter your age: "))

    if age > 24:
        ticket_price = 2.04
    elif age >= 17:
        ticket_price = 1.47
    elif age >= 7:
        ticket_price = 1.02
    else: #age between 0 and 6
        ticket_price = 0.00

    print(f"Your ride will cost: {ticket_price}")

if __name__ == "__main__":
   main()