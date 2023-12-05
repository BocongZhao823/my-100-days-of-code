# https://docs.python.org/3/tutorial/floatingpoint.html

# Tip Calculator

# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Example Output
# Each person should pay: $19.93

# Hint
# How to round a number to 2 decimal places in Python
# How to limit a float to two decimal places in Python

# Solution
# https://replit.com/@appbrewery/tip-calculator-end


####################################Question####################### 
# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
bill = float(bill)
tip = int(tip)
people = int(people)
answer = (bill / people) * (1 + tip/100)
roundAnswer = round(answer, 2)
print(f"Each person should pay: ${roundAnswer}")


