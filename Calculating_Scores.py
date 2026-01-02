"""
COMP.CS.100 Programming 1
A programming that helps you add up the scores
that various contestants have obtained in a game.
Author: Ifeoma Nwankwo
"""

def main():
    filename = input("Enter the name of the score file: ")
    scores = {}

    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                name = parts[0]
                try:
                    score = int(parts[1])
                    if name in scores:
                        scores[name] += score
                    else:
                        scores[name] = score
                except ValueError:
                    continue  # Skip lines with invalid score values

    print("Contestant score:")
    for name in sorted(scores):
        print(f"{name} {scores[name]}")


if __name__ == "__main__":
    main()