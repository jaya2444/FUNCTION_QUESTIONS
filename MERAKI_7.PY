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