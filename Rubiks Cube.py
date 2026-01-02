"""
COMP.CS.100 Programming 1

Rubik’s Cube contest scorer:
Reads five solve-times (in seconds), drops the single fastest
time and the single slowest time, and prints the average of
the remaining three to two decimal places.

Author: Ifeoma Nwankwo
"""

def main():
    times = []
    for i in range(1, 6):
        t = float(input(f"Enter the time for performance {i}: "))
        times.append(t)

    # Remove exactly one fastest and one slowest time
    times.remove(min(times))   # remove one instance of the minimum
    times.remove(max(times))   # remove one instance of the maximum

    average = sum(times) / len(times)    # len(times) is now 3
    print(f"The official competition score is {average:.2f} seconds.")


if __name__ == "__main__":
    main()