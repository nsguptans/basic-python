#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
num=int(input("enter number"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
#2using input function take two number and then swap the number
num1=int(input("enter first number"))
num2=int(input("enter secong number"))
#swap number
print("before swapping num1 and num2 is",num1, num2)
num1,num2=num2,num1#swap the number using tuple unpacking
print("after swapping",num1,num2)
#3. Write a Program to Convert Kilometers to Miles
kilo_meter=float(input("enter distance in km"))
miles=kilo_meter * 0.621371
print(f"{kilo_meter} killometer is equal to {miles:.2f} miles")
#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
P=200
R=5
T=5
si=P*R*T
print("simple interest is:",si)







