tuple_to_count = eval(input("Enter a tuple to be counted: "))
list_to_count = list(tuple_to_count)  #forceing it to a list
already_used = []
for i in list_to_count:  #Here, a linear iteration algorithm acquires all the required values for checking
    if i not in already_used:
        print("The number of occurences of", i, "is", list_to_count.count(i))
        already_used.append(i)
