# Question 3 (Part 1)

# You have to define a function named isGreaterThan20 in
# which you have to pass two parameters to the function and the first parameter by default should be 20.

def isGreaterThan20(a,b=30):
    if a<b:
        print("b is greater than a")
    else:
        print("a is greater than b")
isGreaterThan20(20)

# Question 3 (Part 2)

# You have to define a function named students and pass a parameter to 
# that function which takes a list of students name(don't use the List)

def students(name):
    print(name)
students(list(("aarti","jaya","rahul","aarohi")))