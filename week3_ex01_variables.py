#Week 3 exercise 1: Variables and Data Types
#Question 1: Variable Assignment and String Manipulation

#TODO: Ask the user for their name and store it in a variable called name
name = input("Please enter your name: ")

#TODO: Ask the user for their age and store it in a variable called age
age = input("Please enter your age: ")

#TODO: Print a greeting message that includes the user's name and age
print(f"Hello, {name}! You are {age} years old.")

#--------------------------------------------------------------------

# Question 2: Interger Operations

#TODO: Ask the user for the length of a rectangle and store it as an interger
length = int(input("Enter the length of the rectangle: "))

#TODO: Ask the user for the width of a rectangle and store it as an interger
width = int(input("Enter the width of the rectangle: "))

#TODO: Calculate the area of the rectangle and store it in a variable called area
area = length * width

#TODO: Print the area of the rectangle
print(f"The area of the rectangle is {area}.")

#--------------------------------------------------------------------------------

# Question 3: Working with Floats

#TODO: Ask the user for a temperature in celcius and store it as a float
temperature_celsius = float(input("Enter the temperature in Celsius: "))

#TODO: Convert the temperature to fahrenheit using the formula
temperature_fahrenheit = (temperature_celsius * 9/5) + 32

print(f"The temperature in Fahrenheit is {temperature_fahrenheit}.")

# TODO: Print the result of the conversion to two decimal places
