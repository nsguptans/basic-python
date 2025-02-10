#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(a,b):
    division=a/b
    print("division is:",division)
div(12,2)
#2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
def square(par1):
    square_value=par1**2
    print("square of number is:",square_value)
square(12)
#3. Using max() and min() functions display the maximum and minimum of 5 random numbers
import random
def find_max_min():
    numbers=[random.randint(1,100)for _ in range(5)]
    print("random number",numbers)
    print("maximum value:",max(numbers))
    print("minimum value:",min(numbers))
#4 Accept a name from the user and display that in lower case using lower() function
name=input("enter your name")
print("lower case:",name.lower())






