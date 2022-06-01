# Question (Part 1)

# Create a function named Calculator which takes three arguments - number_x, number_y, operation. number_x and number_y we will take two integers and operation parameter defines the type of mathematical operation to be performed on the two integers.
# For ex:
# If "add" is given in the operation, it will return numberx and numbery by adding it.
# If "subtract" is given in the operation, it will subtract numberx and numbery and return it.
# If "multifly" is given in the operation, it will multifly numberx and numbery and return it.
# If "divide" is given in the operation, it will divide numberx and numbery and return it.
# Below are examples of some function calls:
# Calling calculator(20, 25, "add") will return 45. 45 we will get by doing 20+25.
# Calling Calculator(40, 3, "Subtract") will return 37 on calling. 37 we will get by doing 40-3.
# Calling Calculator(10, 4, "Multiply") will return 40. We will get 40 by doing 10*4.
# Calling calculator(40, 4, "Divide") will return 10 for the call reason. We will get 10 by doing 40/3.
# After writing the function, to do this function call the function and put the value in the variable.
# Add 24 and 20 and put the value in the number_1 variable
# Multiply 50 and 60 and put the value in the number_2 variable
# Divide 80 and 120 and put the value in the number_3 variable
# Subtract 90 and 23 and put the value in the number_4 variable..........................


def calculator(number_x,number_y,operation):
    if operation=="+":
        print(number_x+number_y)
    elif operation=="-":
        print(number_x-number_y)
    elif operation=="*":
        print(number_x*number_y)
    elif operation=="/":
        print(number_x/number_y)
calculator(20,20,"+")
calculator(40,30,"-")
calculator(40,60,"*")
calculator(40,10,"/")
   
# Question (Part 2)

# Now using input take 2 numbers input from the user.
# Note: Not neccesary to create any fuction.
# Call the calculator function 4 times again and again to add, substract, multifly, divide the 
# two numbers and show the result in 4 different variables.
# Those variables would be named as:
# add_result (store the add operation result)
# subtract_result (store the subtract operation result)
# multiply_result (store the multiple operation result)
# divide_result (store the divide operation result)
# Then print the above four variables.
# submit your final code..................................


def calculator(number_x,number_y,operation):
    if operation=="+":
        number_1=number_x+number_y
        print(number_1)
    elif operation=="-":
        number_2=number_x-number_y
        print(number_2)
    elif operation=="*":
        number_3=number_x*number_y
        print(number_3)
    elif operation=="/":
        number_4=number_x/number_y
        print(number_4)
calculator(24,20,"+")
calculator(90,23,"-")
calculator(50,60,"*")
calculator(80,120,"/")

### USE OPERATORS WITH THE INPUTS.......................


def my_function(operation):
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    if operation=="+":
        print(a+b)
    elif operation=="-":
        print(a-b)
    elif operation=="*":
        print(a*b)
    elif operation=="/":
        print(a/b)
my_function("+")
my_function("-")
my_function("*")
my_function("/")

# Write the code of a function named list_change which take 2 lists as integer arguments and then multiply the items of those lists which are on the same index number (order) and get them to return a new list.
# You have to use calculator function to multiply. Can't multiply normally.
# If we call the function like this:
# Code Example
# multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
# Here the value should be multiple_list :
# Code Example
# [10, 200, 150, 100]
# 10 is obtained by multiplying 5 and 2, 200 by multiplying 10 and 20, 150 by 50 and 3, 100 by 20 and 5.

def list_change(number1_list,number2_list):
    a=[]
    i=0
    j=0
    while i<len(number1_list):
        a.append(number1_list[i]*number2_list[j])
        i=i+1
        j=j+1
    print(a)
list_change([5,10,50,20],[2,20,3,5])
# Question (Part 1)

# Write a function named check_numbers which takes two numbers and then print "both are even" 
# if both numbers are even (divide by 2) otherwise print "both numbers are not even".


def check_numbers(a,b):
    # a=20
    # b=10
    if a and b %2==0:
        print("both are even")
    else:
        print("both are not even")
check_numbers(20,10)

# Question (Part 2)

# Now write a function named check_numbers_list Which takes the list of an integer as a argument and 
# then checks whether both the integers with the same index are even or not.
# To check this, use the check_numbers function written in the previous Part 1.
# If you call your function [2, 6, 18, 10, 3, 75] and [6, 19, 24, 12, 3, 87] then it should
# give this output:
# both are even
# both are not even
# both are even
# both are even
# both are not even


def check_numbers():
    a=[2, 6, 18, 10, 3, 75] 
    b=[6, 19, 24, 12, 3, 87]
    i=0
    j=0
    while i<len(a):
        if a[i] and b[j]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i=i+1
        j=j+1
check_numbers()
# Write a function named add_numbers which takes two numbers as
# arguments and then prints their sum.
# The name of the arguments should be number1 and number2.....................

def add_numbers(a,b):
    c=a+b
    print(c)
add_numbers(2,4)


# Write a function named add_numbers_list which takes 2 lists of two integers and then 
# prints the sum of the integers with the same position.
# Use the add_numbers function given in Part 1 to count 2 integers that have the same position.
# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this
# 60
# 80
# 23................


def add_numbers_list():
    a=[50,60,10]
    b=[10,20,13]
    i=0
    j=0
    while i<len(a):
        print(a[i]+b[j])
        i=i+1
        j=j+1
add_numbers_list()