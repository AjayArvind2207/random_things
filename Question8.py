list_to_count = eval(input("Enter a list to count frequency in"))
already_used = []  #list of letters which have already been counted
for i in list_to_count:
    if i not in already_used:
        print("The number of occurences of", i, "is", list_to_count.count(i))  #uses the inbuilt count method to perform the task
        already_used.append(i)
