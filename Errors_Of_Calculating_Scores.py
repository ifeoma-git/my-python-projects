"""
COMP.CS.100 Programming 1
A Program that handles error
Author: Ifeoma Nwankwo
"""

def main():
    filename = input("Enter the name of the score file: ")

    scores = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                # Skip empty lines (optional)
                if not line:
                    continue

                parts = line.split()
                if len(parts) != 2:
                    print("There was an erroneous line in the file:")
                    print(line)
                    return

                name, score_str = parts

                try:
                    score = int(score_str)
                except ValueError:
                    print("There was an erroneous score in the file:")
                    print(score_str)
                    return

                # Accumulate the score
                if name in scores:
                    scores[name] += score
                else:
                    scores[name] = score

        # Print results in alphabetical order
        print("Contestant score:")
        for name in sorted(scores):
            print(f"{name} {scores[name]}")

    except OSError:
        print("There was an error in reading the file.")

# Ensure the main function is called
if __name__ == "__main__":
    main()