# Question 1: Create and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "banana", "orange"]

# TODO: Add a fruit to the end of the list
fruits.append("grape")

# TODO: Insert a fruit at the beginning of the list 
fruits.insert(0, "mango")
# TODO: Remove a fruit from the list 
fruits.remove("banana")
# TODO: Print the modified list
print(fruits)

#----------------------------------------------------------------------------------

# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# TODO: Create a new list with  each number squared
squared_numbers = [x**2 for x in numbers]

# TODO: Find the sum and average of the original numbers
total = sum(numbers)
average = total / len(numbers)

# TODO: Print the results
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Sum:", total)
print("Average:", average)

#----------------------------------------------------------------------------------

# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

# TODO: Add a new country-capital pair
countries_capitals["Germany"] = "Berlin"

# TODO: Update the capital of an existing country
countries_capitals["USA"] = "New York"

# TODO: Print the modified dictionary
print("Modified countries and capitals:", countries_capitals)

# TODO: Remove a country-capital pair
del countries_capitals["France"]

# TODO: Print the modified dictionary
print("Modified countries and capitals:", countries_capitals)

#------------------------------------------------------------------------------------

# Question 4: Dictionary Operations 

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange"
}

# TODO: Print all the fruits (keys)
print("Fruits:", list(fruit_colors.keys()))

# TODO: Print all the colors (values)
print("Colors:", list(fruit_colors.values()))

# TODO: Print each fruit and its color 
for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color
if "apple" in fruit_colors:
    print("Apple color:", fruit_colors["apple"])
    print("Grape color:", fruit_colors.get("grape", "Not found"))
    

