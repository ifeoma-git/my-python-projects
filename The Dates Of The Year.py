"""
Prints all the dates of a non-leap year.

Author: [Ifeoma Nwankwo]
"""

def main():
    #Days in each month for a non-leap year
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    #Outer loop for each month
    for month in range(1, 13):
        #Inner loop for each day in the current month
        for day in range(1, days_in_month[month] + 1):
            print(day,".", month,".", sep= "")

if __name__ == "__main__":
    main()