list_tuple = eval(input("Enter a list or a tuple"))
for i in range(0,len(list_tuple),2):  #ranging through only the even terms to perform swapping
    try:
        list_tuple[i], list_tuple[i+1] = list_tuple[i+1], list_tuple[i]  #swapping even terms and odd terms using multiple assignment
    except:
        break

    '''
A try-except structure is used
So as to avoid the case where the
Number of terms is even, which would
result in issues
'''

    
print("Sorted iterable =",list_tuple)
