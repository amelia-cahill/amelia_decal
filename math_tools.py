#1 Create a Module
#1. Create a Python file called math tools.py.
#2. Inside of this file, define the following functions:
#• add(a, b): Returns the sum of a and b.
#• subtract(a, b): Returns the difference between a and b.
#• multiply(a, b): Returns the product of a and b.
#• divide(a, b): Returns the quotient of a divided by b (handle divi-
#sion by zero).
#3. Make sure each function has a docstring (comment) explaining what it
#does.

def add(a, b):
    """
    Returns the sum of a plus b.
    
    Parameters:
    a (int, float): The first number to be added.
    b (int, float): The second number to be added.
    
    Returns:
    int, float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference between a and b.
    
    Parameters:
    a (int, float): The minuend.
    b (int, float): The subtrahend.
    
    Returns:
    int, float: The difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.
    
    Parameters:
    a (int, float): The first number to be multiplied.
    b (int, float): The second number to be multiplied.
    
    Returns:
    int, float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of a divided by b.
    If b is zero, returns a message indicating division by zero is not possible.
    
    Parameters:
    a (int, float): The numerator.
    b (int, float): The denominator.
    
    Returns:
    float or str: The quotient of a divided by b or a message if division by zero.
    """
    if b == 0:
        return "UND: You can't divide by 0"
    return a / b
