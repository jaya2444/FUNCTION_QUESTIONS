# DOCUMENTS QUESTIONS:-

# Q1.Write a Python program to count the number of strings where the string length is 2
# the first and last characters are the same from a given list of strings.
# list=['abc', 'xyz', 'aba', '1221']
# result= 2.

# def my_function():
#     a=["abc","1221","dcad","tant","jaj"]
#     i=0
#     count=0
#     while i<len(a):
#         if a[i][0]==a[i][-1]:
#             count+=1
#         i=i+1
#     print(count)
# my_function()

# Q2. Write a Python function to find the Max of three numbers.
 
# def my_function(a):
#     i=0
#     max=0
#     while i<len(a):
#         if a[i]>max:
#             max=a[i]
#         i=i+1
#     print(max)
# my_function([2,9,10])

# Q3.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20.

# def my_function():
#     list=[8,2,3,0,7]
#     i=0
#     sum=0
#     while i<len(list):
#         sum=sum+list[i]
#         i=i+1
#     print(sum)
# my_function()

# Q4.Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".       

# def my_function():
#     a="1234abcd"
#     i=1
#     while i<=len(a):
#         print(a[-i],end="")
#         i=i+1
# my_function()
        
# Q5.Write a Python function that takes a list and returns a new list with unique elements of the
# first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

# def my_function():
#     simple_list=[1,2,3,3,3,3,4,5]
#     i=0
#     unique_list=[]
#     while i<len(simple_list):
#       if simple_list[i] not in unique_list:
#         unique_list.append(simple_list[i])
#       i=i+1
#     print(unique_list)
# my_function()

# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].

# def my_function():
#     list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#     i=0
#     b=[]
#     while i<len(list):
#         if list[i]%2==0:
#             b.append(list[i])
#         i=i+1
#     print(b)
# my_function()


# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

# def bmi():
#     weight=float(input("enter the weight"))
#     height=float(input("enter the height"))
#     bmi=weight/height
#     if bmi<=18.5:
#         return "underweight"
#     if bmi<=25.0:
#         return "normal"
#     if bmi<=30.0:
#         return "overweight"
#     if bmi >30:
#         return "obese"
# print(bmi())
    
# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and
# lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

# def my_function():
#     a="the quick Brow fox"
#     i=0
#     count=0
#     count1=0
#     while i<len(a):
#         if a[i]>="a" and a[i]<="z":
#             count=count+1
#         elif a[i]>"A" and a[i]<="Z":
#             count1=count1+1
#         i=i+1
#     print("number of lowecase",count)
#     print("number of uppercase",count1)
# my_function()

# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

# def my_function():
#     i=0
#     l=[]
#     l1=[]
#     while i<=30:
#         if i>0 and i<6 :
#             l.append(i**2)
#         elif i>25 and i<=30:
#             l1.append(i**2)
#         i=i+1
#     print(l,l1)
# my_function()

# Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the
# sum (also as a string):
# "4", "5" --> "9"
# "34", "5" --> "39"
# Notes:
# If either input is an empty string, consider it as zero.

# def my_function():
#     a=(input("enter the number"))
#     b=(input("enter the number"))
#     c=int(a)+int(b)
#     d=str(c)
#     print(type(a))
#     print(type(b))
#     print(d)
#     print(type(d))
# my_function()

# Q11.Implement a function named generateRange(min, max, step), which takes three arguments and
# generates a range of integers from min to max, with the step. The first integer is the minimum value,
# the second is the maximum of the range and the third is the step. (min < max)
# Task
# Implement a function named
# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
# Note
# min < max
# step > 0
# the range does not HAVE to include max (depending on the step)

# def generateRange(a,b,c):
#     print((a,b,c))
#     l=[]
#     for i in range(a,b,c):
#         l.append(i)
#     print(l)
# a=int(input("enter the starting number that will be min "))
# b=int(input("enter the ending number that will be max "))
# c=int(input("enter the step value"))
# generateRange(a,b,c)


# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105





