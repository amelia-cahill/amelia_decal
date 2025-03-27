import math_tools

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  
        except ValueError:
            print("Invalid input! Please enter a valid number.")

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

def operation(prompt):
    while True:
        try:
            return str(input(prompt))  
        except ValueError:
            print("Invalid input! Please enter a valid operation.")

operation = operation("Enter the operation (add, subtract, multiply, divide): ")

# Perform the calculation based on the operation
if operation == "add":
    result = math_tools.add(num1, num2)
elif operation == "subtract":
    result = math_tools.subtract(num1, num2)
elif operation == "multiply":
    result = math_tools.multiply(num1, num2)
elif operation == "divide":
    result = math_tools.divide(num1, num2)
else:
    result = "Invalid operation! Please choose from add, subtract, multiply, or divide."

print(result)
