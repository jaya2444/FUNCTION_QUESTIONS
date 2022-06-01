# Q49. Write a flowchart which takes an input N. Then input N numbers. Then for each of the N numbers, print
# “even” if the number is even or and “odd” if the number is odd.
# Sample input:
# 7
# 1
# 4
# 23
# 95
# 1203
# 403
# 84
# Sample output:
# Odd
# Even
# Odd
# Odd
# Odd
# Odd
# Even




def my_function():
    i=0
    n=int(input("enter the number"))
    while i<n:
        a=int(input("enter the number"))
        i=i+1
        if a%2==0:
            print("even")
        else:
            print("odd") 
my_function()

