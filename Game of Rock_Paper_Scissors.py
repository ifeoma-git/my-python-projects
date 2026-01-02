def get_choice(player_number):
    """Prompt the specified player to enter their choice.

    Parameters:
    player_number(int): The player number(1 or 2) for display in the prompt.

    Returns:
    str: The player's choice as a single character('R','P', or 'S').
    """
    return input(f"Player {player_number}, enter your choice (R/P/S): ")

def determine_winner(choice1, choice2):
    """
    Determine the winner of a rock-paper-scissors round based on the player's choices.

    Parameters:
    choice1 (str): Player 1's choice('R','P','S').
    choice2 (str): Player 2's choice('R','P','S').

    Returns:
    Str: A string declaring the result: "it's a tie!","Player1 won!", or "Player2 won!".
    """
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == "R" and choice2 == "S") or \
         (choice1 == "S" and choice2 == "P") or \
         (choice1 == "P" and choice2 == "R"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

def main():
    Player_1 = get_choice(1)
    Player_2 = get_choice(2)
    result = determine_winner(Player_1, Player_2)
    print(result)

main()

