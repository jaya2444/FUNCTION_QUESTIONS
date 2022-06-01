#  Q29. Write a function that returns the sum of multiplesof 3 and 5 between 0 andlimit(parameter).
# For example, if limit is 20, it shouldreturn the sum of 3, 5, 6, 9, 10, 12, 15, 18,20.

def my_function(a):
    i=1
    sum=0
    while i<=a:
        if i%3==0:
            print(i)
            sum=sum+i
        elif i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print(sum)
my_function(20)