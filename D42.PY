# Q42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

def my_function():
    list=[12, 67, 98, 34]
    i=0
    b=[]
    while i<len(list):
        a=list[i]%10
        list[i]=list[i]//10
        b.append(a+list[i])
        i=i+1
    print(b)
my_function()


