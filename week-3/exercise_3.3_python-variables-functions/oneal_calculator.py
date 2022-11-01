"""
    Title: Exercise 3.3 calculator.py
    Author: Chad ONeal
    Date: 10/31/22
    Description: Exercise 3.2
"""

# functions with returns
def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def divide (x, y):
    return x / y

def multiply (x, y):
    return x * y

# variables to test each function
num1 = 4
num2 = 10
num3 = 6
num4 = 8
num5 = 2

# variable to hold values from above methods
add_total = add(num1, num1)
sub_total = subtract(num2, num3)
div_total = divide(num4, num5)
mul_total = multiply(num2, num5)

# variable to hold string output
output = "4 + 4 is {0}\n10 - 6 is {1}\n8 / 2 is {2}\n10 * 2 is {3}\n".format(add_total, sub_total, div_total, mul_total)

print(output)