# Q1.Write a Python program to count the number of strings where the string length is 2
# the first and last characters are the same from a given list of strings.
# ist=['abc', 'xyz', 'aba', '1221']
# result= 2.
# or more and

def my_function():
    a=["abc","1221","dcad","tant","jaj"]
    i=0
    count=0
    while i<len(a):
        if a[i][0]==a[i][-1]:
            count+=1
        i=i+1
    print(count)
my_function()
