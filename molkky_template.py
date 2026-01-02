"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.

Author: Ifeoma Nwankwo
"""

class Player:
    """
    Represents a Mölkky player and handles their scoring logic.
    """

    def __init__(self, name):
        """
        Initializes a new player with a name and zeroed stats.
        """
        self.name = name
        self.total_points = 0
        self.scores = []
        self.successful_hits = 0

    def get_name(self):
        """
        Returns the player's name.
        """
        return self.name

    def get_points(self):
        """
        Returns the player's current total points.
        """
        return self.total_points

    def has_won(self):
        """
        Returns True if the player's points are exactly 50, else False.
        """
        return self.total_points == 50

    def add_points(self, pts):
        """
        Adds points to the player's total. Applies penalty rules and
        handles feedback like warnings and cheers.
        """
        self.scores.append(pts)

        # Count successful hits
        if pts > 0:
            self.successful_hits += 1

        # Update total points first
        self.total_points += pts

        # Handle penalty for exceeding 50
        if self.total_points > 50:
            print(f"{self.name} gets penalty points!")
            self.total_points = 25
            return  # No need to check cheers or warning if penalty applied

        # Print warning if score is between 40 and 49 inclusive
        if 40 <= self.total_points <= 49:
            missing = 50 - self.total_points
            print(f"{self.name} needs only {missing} points. It's better to avoid knocking down the pins with higher points.")

        # Print cheers if current throw is above average
        if len(self.scores) > 1:
            avg = self.average()
            if pts > avg:
                print(f"Cheers {self.name}!")

    def average(self):
        """
        Returns the average of all entered scores for this player.
        """
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def success_percentage(self):
        """
        Returns the percentage of throws with score > 0, formatted to 1 decimal place.
        """
        total_throws = len(self.scores)
        if total_throws == 0:
            return 0.0
        return round((self.successful_hits / total_throws) * 100, 1)


def main():
    """
    Main game loop for the Mölkky game simulation.
    Handles turns, input, and prints the scoreboard.
    """
    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:
        if throw % 2 == 0:
            in_turn = player1
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.success_percentage()}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.success_percentage()}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()

