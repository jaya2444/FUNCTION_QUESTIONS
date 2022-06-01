# Q17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting
# to be 18. )



def my_function():
    age=int(input("enter the age"))
    if age>=18:
        print("able to vote")
    else:
        print("not able to vote")
my_function()