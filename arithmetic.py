"""
Module for basic arithmetic operations.
"""

def add(a, b):
    """
    Function to add two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Function to subtract two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The result of a - b.
    """
    return a - b

def multiply(a, b):
    """
    Function to multiply two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Function to divide two numbers.
    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.
    Raises:
        ValueError: If b is zero.
    Returns:
        int or float: The result of a / b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b