# Question 6
# Define a function that checks the speed of drivers. This function will take a parameter named speed, and will satisfy the following conditions:
# 1.If speed if less than 70, print 70.
# 2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
# 3. If points are more than 12, print “License suspended”
# Input:-
# 85
# 135
# Output :-
# 3
# “License suspended”




def check_speed(speed):
    if speed<70:
        print("70")
    elif speed>70:
        a=speed-70
        b=a//5
        if b>12:
            print("licenses suspended")
        else:
            print(b)
user_input=int(input("enter the number"))
check_speed(user_input)