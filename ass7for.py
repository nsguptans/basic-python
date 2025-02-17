#1. program to print factorial of a number.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i

    
    print(f"Factorial of {num} is {factorial}")
#---------------------------------------------------
#2Program to check whether the given number is prime or not.
num = int(input("Enter a number: "))

# Check if the number is prime
if num < 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
#-----------------------------------------------------------
''' 3. program to display the patterns.

1

1 2

1 2 3

1 2 3 4

1 2 3 4 5'''
n = int(input("Enter the number of rows: "))

# Loop to generate the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

      
        




