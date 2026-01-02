def main():
    player1 = input("Player1, enter your choice (R/P/S): ")
    player2 = input("Player2, enter your choice (R/P/S): ")
    if player1 == player2:
        print("it's a tie!")
    elif (player1 == 'P' and player2 == 'R') or \
         (player1 == 'R' and player2 == 'S'):
        print("player1 won!")
    else:
        print("player2 won!")

main()

