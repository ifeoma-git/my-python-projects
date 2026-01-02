"""
This program asks the user how many Fibonacci numbers they want,
and prints that many numbers from the Fibonacci sequence,starting from 1.
Each number is printed on its own line with its position in the sequence.

Author: Ifeoma Nwankwo
"""

def main():
    count = int(input("How many Fibonacci numbers do you want? "))

    previous_fib = 0
    current_fib = 1

    for i in range(1, count + 1):
        print(f"{i}. {current_fib}")
        next_fib = previous_fib + current_fib
        previous_fib = current_fib
        current_fib = next_fib

if __name__ == "__main__":
   main()
