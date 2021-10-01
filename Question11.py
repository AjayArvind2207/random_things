list_tuple = eval(input("Enter a list or tuple to be bubble-sorted: "))
'''
Bubble sort algorithm

Best case is utilized here
Time complexity: O(N^2)

Bubble sort algorithms help to bubble the numbers up by placing heavier numbers at the bottom
'''


for i in range(len(list_tuple)):
    for l in range(len(list_tuple)-1-i):
        if list_tuple[l] > list_tuple[l+1]:   #if the required number is greater
            list_tuple[l], list_tuple[l+1] = list_tuple[l+1], list_tuple[l]  #perform the swapping
print("Sorted list: ", list_tuple)
