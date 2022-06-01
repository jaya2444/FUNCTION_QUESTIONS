# Q30. Write a function that prints all the prime numbers between 0 and limit where limit is a
# parameter.

def my_function(a):
    i=1
    while i<=a:
        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0:
            print(i)
        elif i==2 or i==3 or i==5 or i==7 or i==11:
            print(i)
        i=i+1
my_function(100)