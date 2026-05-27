# Question 1: Using a for loop with a list

# TODO: Create a list of fruitsfrom random i

fruits = ["apple", "banana", "orange"]


# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    print(i**2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random


# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]

# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(colors))


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import custom_calculator as calculator # type: ignore


# TODO: Use a while loop to create a simple calculator
while True:
    operation = input("Enter an operation (add, subtract, multiply, divide) or 'exit' to quit: ")
    if operation == "exit":
        break
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operation == "add":
        print(calculator.add(num1, num2)) # type: ignore
    elif operation == "subtract":
        print(calculator.subtract(num1, num2)) # type: ignore
    elif operation == "multiply":
        print(calculator.multiply(num1, num2)) # type: ignore
    elif operation == "divide":
        print(calculator.divide(num1, num2)) # type: ignore
    else:
        print("Invalid operation. Please try again.")
        