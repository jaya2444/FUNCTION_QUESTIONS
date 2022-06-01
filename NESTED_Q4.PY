# Question 4
# Define a function which takes one argument which is the limit upto which the function has to print the numbers and their label(even or odd) as shown below.
# For example :-
# Input:-
# 3
# Output :-
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


def my_function(a):
    i=0
    while i<=a:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i=i+1
my_function(3)





