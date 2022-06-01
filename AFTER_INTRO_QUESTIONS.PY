# Question 1
# What will be the output of the code given below?

# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")
# # op=kartik your salary is:-30000
# #    deepak your salary is:-20000



# # Question 3
# What will be the output of the code given below?


# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# op=Hello sonu 
#    Helllo kartik
#    Hello umesh 
#    Hello bijender




# Question 4
# What will be the output of the code given below?

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#         return sum
# print(sumofdigits(123)) 
# # op=3 

   
# Question 5
# What will be the output of the code given below?

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))


# output=dal rice 
#        chhole bhature


# Question 6
# What will be the output of the code given below?

# def checkKey():
#     car={
#         "brand":  "ford",
#         "model":  "mustang",
#         "year":  1964
#     }
#     if "model" in car:
#         print("Yes, 'model' is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.")

# checkKey()

# output=Yes, 'model' is one of the keys in the thisdict dictionary.")



