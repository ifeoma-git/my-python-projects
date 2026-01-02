# Ask the user for the current amount of study benefits
benefit = float(input("Enter the amount of the study benefits: "))

# First index raise
first_raise = benefit * (1 + 1.17/100)

# Second index raise applied to the already raised benefit
second_raise = first_raise * (1 + 1.17/100)

# Print results
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", first_raise, "euros")
print("and if there was another index raise, the study")
print("benefits would be as much as", second_raise, "euros")