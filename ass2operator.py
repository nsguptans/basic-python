#1. write a rogram to accept a number and dsiplay its square and cube.
'''num=int(input("enter number"))
sqaure=num**2
cube=num**3
print("square of number is:",sqaure)
print("cube of number is",cube)'''
#2. write a program to accept 5 float values and display its sum and average.
numbers=[]
for i in range(5):
    num=float(input("enter 5 number:"))
    numbers.append(num)
    total_sum=sum(numbers)
    average=total_sum/len(numbers)

print("sum is:",total_sum)
print("average is:",average)
#3. write a program to calculate the area of rectangle.
length=float(input("enter length"))
width=float(input("enter width"))
area=length*width
print("the area of rectangle is",area)



