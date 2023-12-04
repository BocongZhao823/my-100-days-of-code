# https://app.auditorium.ai/courses

# Print Function 
print("Hello World!")
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Windows: Ctrl + Enter
print("Hello world!\nHello world!")
print("Hello" + "Angela")
print("Hello" + " " + "Angela")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Input Function --> output: Hello name
input("What is your family name?")
print("Hello " + input("What is your first name?"))

# Windows: ctrl + /
# print("comment all")
# Windows: ctrl + z --> undo

# If input Jane --> output 4
print(len(input("What's your name?")))


# Variable 
name = input("What is your name")
print(name)

name = "Angela"
print(name)

# print (len (input ("What is your name again?")))
name = input ("What is your name again?")
length = len(name)
print(length)

# Exercise 
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b 
b = c
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
