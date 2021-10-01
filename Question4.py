list_tuple = eval(input("Enter a list or a tuple")) 
element_to_search = input("Enter the element to be searched in the iterable: ")
if element_to_search in list_tuple:   #linear search by iterating through each element --> O(N) complexity
    print("Element found at position",list_tuple.index(element_to_search))
else:
    print("No occurence of the element in the list")
