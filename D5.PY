# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

def my_function():
    a=[1,2,3,3,3,3,3,4,5]
    i=0
    unique_list=[]
    while i<len(a):
        if a[i] not in unique_list:
            unique_list.append(a[i])
        i=i+1
    print("unique_list",unique_list)
my_function()
