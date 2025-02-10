#Q.1 print helloworld
print("hello world")
#Q.2 describe local variable and global variable code
x=10
def my_function():
    y=20
    print("local variable",y)
    print("global variable",x)
my_function()
#Q.3 Write a code that describe Indentation error
'''def my_function():
    print("helllo")
    print("world")
    if True:
 print("true")#incorrect indentation
    print("corrrect indentation")
my_function()'''
#Q.4 write a code that describe local and global variable with same name
#globle variable
x=89
def my_function():
    #local variable with same nme
    x=90
    print("local vriable",x)
my_function()
print("global variable",x)
#Q.5 Write a code for string, int and float input.
#string input
name= input("enter your name")
print("hello" + name +"!")
#integer input
age=int(input("enter your age"))
print("your age is",age)
#float input
height=float(input("enter your height"))
print("youe height is:",height)





