# Q32.Complete the function that takes a non-negative integer n as input, and returns a list of
# all the powers of 2 with the exponent ranging from 0 to n (inclusive).
# n=0 == >[1] #[2^0]
# n = 1 ==> [1, 2] # [2^0, 2^1]
# n = 2 ==> [1, 2, 4] # [2^0, 2^1, 2^2].

def my_function():
    n=int(input("enter the power"))
    a=2
    i=0
    b=[]
    while i<=n:
        b.append(a**i)
        i=i+1
    n=n+1
    print(b)
my_function()
