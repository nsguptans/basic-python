#1. Write a python program to reverse a number using a while loop.
num = int(input("Enter a number: "))
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10  
    return reversed_num
print("Reversed number:", reverse_number(num))
#2. Write a python program to check whether a number is palindrome or not?

num = int(input("Enter a number: "))
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10  
    return reversed_num
def is_palindrome(n):
    return n == reverse_number(n)
if is_palindrome(num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
#3. Write a python program finding the factorial of a given number using a while loop.
    # Input from user
num = int(input("Enter a number: "))
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    while n > 0:
        result = result*n
        n = n-1
    return result

print(f"Factorial of {num} is {factorial(num)}")
#4 Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
num=int(input("enter a number"))
total=0
while True: 
 if num==0:
    break
total=total+num
print(" total number:",total)
 








    








     
    

