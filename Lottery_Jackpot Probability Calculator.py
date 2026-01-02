"""
COMP.CS.100 Programming 1
lottery-Jackpot Probability Calculator

The probability of guessing all p drawn balls out of n is 1 / [n! / ((n - p)! . p!)].
Author: Ifeoma Nwankwo
"""

#____________________Functions______________________________

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combinations(n, k):
    """
    Calculates the number of combinations (n choose k), i.e.,
    the number of ways to choose k items from n items without repetition.

    Parameters:
        n (int): The total number of items.
        k (int): The number of items to choose.

    Returns:
        int: The number of possible combinations.
    """
    return factorial(n) // (factorial(k) * factorial(n - k))

def main():
    total = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))

    if total <= 0 or drawn <= 0:
        print("The number of balls must be a positive number.")
        return
    elif drawn > total:
        print("At most the total number of balls can be drawn.")
        return
    probability = combinations(total, drawn)
    print(f"The probability of guessing all {drawn} balls correctly is 1/{probability}")

if __name__ == "__main__":
    main()


