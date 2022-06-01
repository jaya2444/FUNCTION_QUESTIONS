# Q4.Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".
def string_reverse(str1):
    a = ''
    i = len(str1)
    while i > 0:
        a=a+str1[ i - 1 ]
        i = i- 1
    return a
print(string_reverse('1234abcd'))



