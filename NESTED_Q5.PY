# Question 5
# Define a function which takes one parameter(positive integer). This function returns the sum of all multiples of 3 and 5 (not neccessary common multiples) in the range 1 to the integer passed as the parameter.
# Input:-
# 10
# 3 aur 5 ke multiples => 3, 5, 6, 9, 10
# Output :-
# 33





def my_function(a):
    i=1
    sum=0
    while i<=a:
        if i%3==0:
            print(i)
            sum+=i
        elif i%5==0:
            print(i)
            sum+=i
        i=i+1
    print(sum)
my_function(10)


    

