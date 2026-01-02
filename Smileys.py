def get_user_input():
    """Ask the user for input and return it as a string."""
    return input("How do you feel? (1-10) ")

def is_valid_input(user_input):
     """Check if the input is a digit and within the valid range (1-10)"""
    return user_input.isdigit() and 1 <= int(user_input) <= 10

def get_smiley(feeling):
    """Return the appropriate smiley based on the feeling value."""
    if feeling == 1:
        return ":'("
    elif 2 <= feeling <= 3:
        return ":-("
    elif 4 <= feeling <= 7:
        return ":-|"
    elif 8 <= feeling <= 9:
        return ":-)"
    elif feeling == 10:
        return ":-D"

def main():
    user_input = get_user_input()

    if is_valid_input(user_input):
        feeling = int(user_input)
        smiley = get_smiley(feeling)
        print("A suitable smiley would be", smiley)
    else:
        print("Bad input!")
#Run the program
main()

