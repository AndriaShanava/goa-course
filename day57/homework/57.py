# Python Syntax

# 1. Print "Hello, World!"

print("Hello, World!")

# 2. Take user input and print it python

user_input = input("Enter something: ")
print("You entered:", user_input)

# 3. Use single-line and multi-line comments

# This is a single-line comment

'''
This is a multi-line comment.
It can span multiple lines.
'''
print("Comments demonstration")

# 4. Demonstrate indentation in Python

if True:
    print("This is properly indented.")
    if True:
        print("This is further indented.")

# 5. Break lines in Python

long_string = "This is a very long string that we can " \
              "break into multiple lines using the backslash character."
print(long_string)


# Python Comments

# 1. Add comments to explain each line

# Define a variable
x = 10

# Print the value of the variable
print("The value of x is:", x)

# 2. Explain a function's purpose

def greet(name):
    # This function takes a name as input and prints a greeting
    print("Hello, " + name + "!")
greet("Alice")

# 3. Block comment to describe overall functionality

"""
This script demonstrates basic arithmetic operations in Python.
It includes addition, subtraction, multiplication, and division.
"""
a = 5
b = 3
print(a + b)

# 4. Disable a part of the script

x = 10
# print("This line is disabled")

print("This line is enabled")

# 5. Intentional errors and comments

# The following line will cause a syntax error because of the missing closing parenthesis
# print("This will cause an error

# Uncommenting the next line will cause a NameError because 'y' is not defined
# print(y)

# Python Variables

# 1. Create and initialize multiple variables

integer_var = 10
float_var = 20.5
string_var = "Hello"
bool_var = True

# 2. Swap the values of two variables

a = 5
b = 10

# Swap
a, b = b, a

print("a:", a)
print("b:", b)

# 3. Assign values to variables using user input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Name:", name)
print("Age:", age)

# 4. Global and local variables

x = "global"

def my_function():
    x = "local"
    print("Inside function:", x)

my_function()
print("Outside function:", x)

# 5. Variable naming conventions

my_variable = 10
another_variable = 20
_private_variable = 30
camelCaseVariable = 40


# Python Data Types

# 1. Create variables of different types

integer_var = 10
float_var = 20.5
string_var = "Hello"
boolean_var = True

# 2. Convert between different data types

x = 10
print(type(x))

# 3. Use type() to check variable types

x = 10
print(type(x))

# 4. Basic arithmetic operations

a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 5. Compare different data types

x = 10
y = "10"
print(x == int(y))


# Python Numbers

# 1. Perform arithmetic operations

a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 2. Generate a random number

import random
print(random.randint(1, 100))

# 3. Calculate square root

import math
print(math.sqrt(16))

# 4. Use ceil() and floor() functions

import math
x = 4.7
print(math.ceil(x))
print(math.floor(x))

# 5. Find the greatest common divisor (GCD)

import math
print(math.gcd(24, 36))



# Python Casting

# 1. Convert integers to floats and vice versa

a = 5
b = 3.2
print(float(a))
print(int(b))

# 2. Convert strings to integers and floats

a = "10"
b = "3.14"
print(int(a))
print(float(b))

# 3.Casting between lists and tuples

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)
my_list_again = list(my_tuple)
print(my_list_again)

# 4. Handle casting errors

a = "10a"
try:
    b = int(a)
except ValueError:
    print("Cannot cast '10a' to an integer")

# 5. Convert a string representing a number

num_str = "42"
num_int = int(num_str)
print(num_int)



# Python Booleans

# 1. Demonstrate the use of boolean values

is_day = True
is_night = False

print("Is it day?", is_day)
print("Is it night?", is_night)

# 2. Perform logical operations (and, or, not)

a = True
b = False

print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False

# 3. Comparison operators to return boolean values

x = 10
y = 20

print("x == y:", x == y)    # False
print("x < y:", x < y)      # True
print("x >= y:", x >= y)    # False

# 4. If-else statements based on boolean values

is_raining = True

if is_raining:
    print("Take an umbrella.")
else:
    print("No need for an umbrella.")

# 5. Return a boolean result from a function

def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False



# Python Operators

# 1. Demonstrate arithmetic operators

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a + b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# 2. Use assignment operators

x = 5
x += 3  # Equivalent to x = x + 3
print("x after += 3:", x)

x *= 2  # Equivalent to x = x * 2
print("x after *= 2:", x)

x -= 4  # Equivalent to x = x - 4
print("x after -= 4:", x)

# 3. Show the use of comparison operators

a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)

# 4. Demonstrate the use of logical operators

x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# 5. Use identity operators (is, is not)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)          # True
print("a is c:", a is c)          # False
print("a is not c:", a is not c)  # True




# Python Lists

# 1. Create and print a list

fruits = ["apple", "banana", "cherry"]
print(fruits)

# 2. Add and remove elements from a list

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add
fruits.remove("banana")  # Remove
print(fruits)

# 3. Sort a list

numbers = [4, 2, 9, 1]
numbers.sort()
print("Sorted list:", numbers)

# 4. Use list comprehension

squares = [x**2 for x in range(5)]
print(squares)

# 5. Find the length of a list

fruits = ["apple", "banana", "cherry"]
print("Length of the list:", len(fruits))




# Python If...Else


# 1. Use an if statement to check a condition


x = 10

if x > 5:
    print("x is greater than 5")

# 2. Use an if-else statement

x = 4

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# 3. Use an if-elif-else statement

x = 7

if x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is greater than 5")

# 4. Demonstrate nested if statements

x = 10

if x > 5:
    if x < 15:
        print("x is between 5 and 15")

# 5. Use the ternary operator

x = 8
result = "Even" if x % 2 == 0 else "Odd"
print("x is", result)



# Python While Loops

# 1. Demonstrate a while loop

i = 1

while i <= 5:
    print("i =", i)
    i += 1

# 2. Use a while loop with a break statement

i = 1

while True:
    print("i =", i)
    if i >= 5:
        break
    i += 1

# 3. Use a while loop with a continue statement

i = 0

while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print("i =", i)

# 4. Demonstrate an infinite loop and how to stop it

i = 1

while True:
    print("Infinite loop. Press Ctrl+C to stop.")
    i += 1

# 5. Use a while loop to iterate over a list

fruits = ["apple", "banana", "cherry"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1


# Python For Loops

# 1.Demonstrate a for loop

for i in range(5):
    print("i =", i)

# 2. Use a for loop to iterate over a list
    
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# 3. Use a for loop with the range() function
    
for i in range(1, 6):
    print("i =", i)

# 4. Demonstrate nested for loops

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# 5. Use a for loop with an else clause
    
for i in range(5):
    print("i =", i)
else:
    print("Loop has finished.")

# Python Functions

# 1. Define and call a function

def greet():
    print("Hello, World!")

greet()

# 2. Use a function with parameters

def greet(name):
    print("Hello,", name)

greet("Alice")

# 3. Use a function with a return value

def add(a, b):
    return a + b

result = add(5, 3)
print("Result:", result)

# 4. Demonstrate the use of default parameters

def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Alice")

# 5. Use a function with keyword arguments
    
def describe_person(name, age):
    print(f"Name: {name}, Age: {age}")

describe_person(age=30, name="Alice")
