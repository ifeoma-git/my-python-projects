def main():
    sticks = 21
    current_player = 1

    print("Game of Sticks")

    while sticks > 0:
        try:
           move = int(input(f"Player {current_player} enter how many sticks to remove: "))
        except ValueError:
            print("must remove between 1 - 3 sticks!")
            continue

        if move < 1 or move > 3:
            print("must remove between 1 - 3 sticks!")
            continue

        if move > sticks and sticks <= 3:
            print(f"Player {current_player} lost the game!")
            break

        sticks -= move

        if sticks == 0:
            print(f"Player {current_player} lost the game!")
            break

        else:
            print(f"There are {sticks} sticks left")

            current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    main()