# Function is a code of block that only runs when it is called.
# In the function we pass the data which we call parameter. Function returns data.
# By using functions, we can write some code once and use it many times. This makes our work very easy.
# Functions are also named according to the naming rules of variables.Once memorize the naming rules of variables.
# In Python, just writing the function does not run the code of the function. Here first we told python the code of the function by using the def keyword. It is called "FUNCTION DEFINITION".
# Then we later called the function by writing definition_hello_again() and the written code try to run. It is called as "FUNCTION CALL". In "FUNCTION CALL" we put 2 brackets ( ) after the name of the function. This tells Python that the code inside the function has to run.

# max function, is one of the pre-define function, where no need to defined the def max() to write the code of block because the creator of Python has already done this work for us.
# Similarly, the len function also takes a list and gives us the count of items in the list.
# We use the len( ) function to find the length of an array or sequence. It is also the python pre-define function.
# Example :-
# a=[1,2,3,4,5,6]
# print(len(a))

# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Aatif")
# Notice that the after def say_hello in the function brackets we write name and the bellow of that we write the name variable with the print command. Here the name is called * parameter * whose value we can give at the time of calling the function.While calling the function in the last line, we have written "Atif" inside the brackets. The parameters we assign values ​​while calling a function are called arguments.

# in this example we learn:
# Defined a function named say_hello which takes a parameter named name and prints something using that
# Then we called the function and at the time of calling the function, we gave an argument whose value was "Atif"
# When this function call then which we have given string "Atif" argument. Here its value goes to the name parameter and this value
# name is passed to the parameter, so he can pass it inside the function to a variable named 'name'. We have written the print command by using variable name.

# Multiple Function Arguments-
# We have written the code with only one function argument. Now let's write the code with a few more function arguments.

# def add_numbers(number1, number2):
#     print("I will add two numbers.")
#     print(number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)
# Output :-
# I will add two numbers.
# 170
# I will add two numbers.
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Let's see another example for better understanding.
# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")
# Output :-
# Sat sri akaal Rishabh
# Tuhada ki haal hai?
# Hello Armaan
# How are you?
# Hello Abhishek
# How are you?
# Namaste Kavay
# Aap kaise ho?
# This function takes two parameters, name and languageand works like this:
# If language is "hindi", then should be print something in Hindi.
# If language is "punjabi", then should be print something in Punjabi.
# If "hindi" or "punjabi", you have given any langauge other than this, it will print in English.
# To do this we defined a function that takes two arguments, name and language.When we call say_hello_language("rishabh", "punjabi") see what happens:
# The string value "Rishabh" goes the first parameter which is name and the second parameter, language goes for "punjabi".
# Then our program uses if-elif-else to see what is the value of the language and print it to the correct language accordingly
# This happenes in the every function calls.

# One more example-
# def say_hello_people(name_x, name_y, name_z, name_a):
#     print("Namaste ", name_x) # In hindi
#     print("Alah hafiz ", name_y) # In urdu 
#     print("Bonjour ", name_z) # In french 
#     print("Hello ", name_a) # In english 
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")
# Output :-
# Namaste Imitiyaz
# Alah hafiz Rishabh
# Bonjour Rahul
# Hello Vidya
# Namaste Steve
# Alah hafiz Saswata
# Bonjour Shakrundin
# Hello Rajeev
# See in this function that, it takes 4 arguments, name_x, name_y, name_z, name_a. In the first line of def, we have written the names of 4 parameters with commas (,). The order in which we have written the parameters while calling the function, in the def line, In the same sequence/ order, the values ​​of the arguments go to the parameters.
# The values ​​of the parameters in say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya") are as follows:
# The value of "Imtiyaz" is passed to the first parameter name_x
# The value of "Rishabh"is passed to the first parameter name_y
# The value of "Rahul" is passed to the first parameter name_z
# The value of "Vidya" is passed to the first parameter name_a

# Python Arbitrary Arguments-
# Arbitrary Arguments we use when do not know how many numbers we have of arguments are to be given in the function. We use ( * ) before parameters to define functions with arbitrary arguments as shown below.
# Example:-
# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)
# icecream("chocolate", "butterscotch","vanilla","strawberry")
# Output :-
# i love chocolate
# i love butterscotch
# i love vanilla
# i love strawberry 

# Default parameter value-
# Here by default parameter value, we mean that we assign a value to a parameter while defining the function so that if we call the function without any argument, it will take the default value.
# Example :-
# def attendance(name,status="absent"):
#     print(name,"is",status," today")
# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")
# Output :-
# kartik is present today
# sonu is absent today
# vishal is present today
# Umesh is absent today


