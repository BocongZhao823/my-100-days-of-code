# Data Types

# String
print("Hello"[4])

# Integer
print(123 + 345)

num_char = len(input("What is your name?"))
print(type(num_char))
print("Your name has", num_char, "characters.")
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))

print(str(70) + str(100))


# Exercies
# Instructions: Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.
# The last line of your program should print the result.
# Example 1 Input 39
# Example 1 Output 12
# Example 2 Input 43
# Example 2 Output 7
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
newImput = str(two_digit_number)
firstNum = newImput[0]
secondNum = newImput[1]
newFirstNum = int(firstNum)
newSecondNum = int(secondNum)
print(newFirstNum + newSecondNum)

# operations
3 + 5
7 - 4
3 * 2
print(type(6 / 3))
print(2 ** 3)

# PEMDAS --> () --> ** --> * --> / --> + --> -

print(3 * 3 + 3 / 3 - 3) #--> 7
print( 3 * (3+3) / 3 - 3) # --> 3

# Exerciese 
# Instructions: Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.
# Example Input 1: 1.75, 80
# means: weight = 80 and height = 1.75
# Example Output 1: 26
# Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837
# Example Input 2: 1.58, 57
# Example Output 1: 22
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
height = float(height)
weight = float(weight)
BMI = round (weight/ (height**2))
print(BMI)

print(8/3)
print(int(8/3))
print(round(8/3))
print(round(8/3, 2)) # round two decimal places
print(8 // 3) # Get whole number
print(type(8//3))

result = 4/2
result /= 2
print(result)

score = 0
score += 1
print(score)
score -= 1
print(score)

score = 0 
height = 1.8
isWinning = True
# f-string
print( f"your score is {score}, your height is {height}, you are {isWinning}")


# Exerciese
# Instructions： I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input: 56
# Example Output: You have 1768 weeks left.
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age = int(age)
x = (90 - age) * 52
print(f"You have {x} weeks left.")