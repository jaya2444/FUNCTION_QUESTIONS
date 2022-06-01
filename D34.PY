# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] --> 42 (= 23 + 19)
# [99, 2, 2, 23, 19] --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def my_function():
    a=[]
    size=int(input("enter the size of list"))
    i=0
    while i<size:
        i=i+1
        val=int(input("enter the number"))
        a.append(val)
    print(a)
    maxval=max(a)
    print("max value in list",maxval)
    a.remove(maxval)
    smax=max(a)
    print("second max value in the list",smax)
    print("sum of first max and second max",maxval+smax)
my_function()