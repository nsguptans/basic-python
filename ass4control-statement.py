#1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
num=int(input("enter number"))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
#2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
age=int(input("enter your age"))
if age>18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")
#3.Write a Python program that determines if a given year is a leap year or not.
if year%4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is leap year")
else:
    print("not leap year")
#4.Create a Python program that checks if a user-given number is positive, negative, or zero
number=int(input("enter a number"))
if number>0:
    print(f"{number}is a positive number")
elif number<0:
    print(f"{number}is negative number")
else:
    print(f"{number} is zero")

#5. Write a Python program that determines the largest of three numbers entered by the user.
num1=int(input("enter num1 value"))
num2=int(input("enter num2 value"))
num3=int(input("enter num3 value"))
if num1>num2 and num1>num3:
    print("num1 is largest")
elif num2>num1 and num2>num3:
    print("num2 is largest")
else:
    print("num3 is largest")






