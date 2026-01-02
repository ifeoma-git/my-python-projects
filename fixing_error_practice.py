def main():
    answer = " "
    while answer != 'Y' and answer != 'N':
        answer = input("Answer Y or N: ")

        if answer != 'Y' and answer != 'N':
            print("Incorrect entry")

        else:
            print(f"you answered,{answer}")

if __name__ =="__main__":
    main()