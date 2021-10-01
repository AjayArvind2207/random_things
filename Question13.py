a,b = 0,1

'''
Fibonacci series:

Series in which the nth term is defined as the sum of the (n-1)th and (n-2)th term

A simple for loop structure and multiple assignment is used to make this

Alternatively, recursion can be used for the same
'''


tup = (a,b)
for i in range(7):
    a,b = b,a+b
    tup+=(b,)
print(tup)
