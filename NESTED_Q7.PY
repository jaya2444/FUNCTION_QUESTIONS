# Question 7
# Define a function which takes two arguments(strings) and returns the string with largest length. If both the strings have equal length, print both the strings one below the other.
# Hint :- use len() builtin function..
# Input:-
# Code Example
# # Write function here
# function_name(“hello”,”welcome”)
# function_name(“sonu”,”monu”)
# Output :-
# welcome
# sonu
# monu




# def my_function(a,b):
#     print(b)
#     def my_function2(a,b):
#         print(a)
#         print(b)
#     my_function2("sonu","monu")
# my_function("hello","welcome")



def my_function(a,b):
    i=0
    while i<len(a):
        if len(a)==len(b):
            print(a)
            print(b)
            break
        elif len(a)>len(b):
            print(a)
            break
        else:
            print(b)
            break
        i=i+1
my_function("hello","welcome")
my_function("sonu","monu")