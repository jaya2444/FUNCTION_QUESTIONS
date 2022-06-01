# Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])


def my_function():
    n=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    i=0
    c=0
    while i<len(n):
        j=0
        c1=0
        while j<len(n[i]):
            j=j+1
            c1=c1+1
        i=i+1
    c=c+1
    print("max",(c1,n[-1]))
    print("min",(c,n[0]))
my_function()
