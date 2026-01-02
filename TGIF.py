"""
Prints all the Fridays in the year 2014.

In 2014, the first Friday was on January 3rd (3.1.).
This program goes through all the dates of the year
and prints only the ones that fall on a Friday.

Author: [Ifeoma Nwankwo]
"""

def main():
    #Number of days in each month for a non-leap year (like 2014)
     days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    #Initialize the day of your counter
     day_of_year = 0

     for month in range(1,13):
        for day in range(1,days_in_month [month - 1] + 1):
            day_of_year += 1
            #First Friday was on a day 3 (3.1.), so start counting from there
            if (day_of_year - 3) % 7 == 0:
                print(f"{day}.{month}.")

if __name__ == "__main__":
    main()
