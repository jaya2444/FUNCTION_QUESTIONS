# Q40. Write a function For example, if we give 9119 the function should return 811181, as the square of 9
# is 81 and square of 1 is 1.




def my_function():
    n=int(input("how many elements you want in your list?"))
    i=0
    b=[]
    while i<n:
      i=i+1
      a=int(input("enter the number"))
      b.append(a)
    print(b)
    i=0
    while i<len(b):
          j=(b[i])**2
          i=i+1
          print(j,end="")
my_function()
