# Question 1: Arithmetic Operators
# TODO: Add 3 to x using the += operator
x = 5
x += 3
print(f"After adding 3, x is now: {x}")
# TODO: Multiply y by 2 using the *= operator
y = 4
y *= 2
print(f"After multiplying by 2, y is now: {y}")
# TODO: Divide x by y and store the result in a variable called z
z = x / y
print(f"After dividing x by y, z is now: {z}")
# TODO: Print the value of z
print(f"The value of z is: {z}")
#--------------------------------------------------------------------------------
# Question 2: comparison and logical Operators
# TODO: Create a condition that checks if a is greater than b and print the result
a = 10
b = 5
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
# TODO: Create a condition that checks if b is even (hint: use the modulus operator) and print the result
if b % 2 == 0:
    print("b is even")
else:
    print("b is odd")
# TODO: Create a condition that checks if c is between 1 and 10 (inclusive) and print the result
c = 7
if 1 <= c <= 10:
    print("c is between 1 and 10 (inclusive)")
else:
    print("c is not between 1 and 10 (inclusive)")
# TODO: Combine the above conditions using logical operators to check if a is greater than b and c is between 1 and 10, and print the result
if a > b and 1 <= c <= 10:
    print("a is greater than b and c is between 1 and 10")
else:    print("Either a is not greater than b or c is not between 1 and 10")
# --------------------------------------------------------------------------------
# Question 3: Conditional Statements
# TODO: Ask the user to input a test score (0-100) and store it in a variable called score
score = int(input("Please enter your test score (0-100): "))
# TODO: Implement a grade system using if-elif-else statements: 
# If the score is 90 or above, print "Grade: A"
# If the score is 80-89, print "Grade: B"
# If the score is 70-79, print "Grade: C"
# If the score is 60-69, print "Grade: D"
# If the score is below 60, print "Grade: F"

# TODO: Print the grade based on the score
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#----------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables num1 and num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# TODO: Ask the user to input an operator (+, -, *, /) and store it in a variable called operator
operator = input("Enter an operator (+, -, *, /): ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2 based on the operator input, and store the result in a variable called result
if operator == "+":
    result = num1 + num2

# TODO: Handle the case of division by zero 
# TODO: Print the result of the operation