#  Question (Part 1)

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