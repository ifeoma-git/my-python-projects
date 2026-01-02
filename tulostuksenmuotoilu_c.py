"""
This program prints a formatted multiplication table from 1 to 10,
Each number is displayed in a right-aligned field that is 4 characters wide.
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

if __name__ == "__main__":
    main()
