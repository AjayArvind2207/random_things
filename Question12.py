list_tuple = eval(input("Enter a list or tuple to be insertion-sorted: "))

'''
Insertion sort algorithm


Time complexity: O(N^2)

Insertion sort algorithms help to push down the heavier numbers up by placing lighter numbers at the top
''' 


for i in range(1,len(list_tuple)):
    key = list_tuple[i]  #key is the object of the list on which the sorting occurs
    temp = i-1 #creating a temporary variable to use for index-swapping
    while temp>=0 and key < list_tuple[temp]:
        list_tuple[temp+1] = list_tuple[temp]
        temp-=1
    list_tuple[temp+1] = key   #Reassigning the key variable to perform the sorting on the next object of the list
print("Sorted list:", list_tuple)
        
