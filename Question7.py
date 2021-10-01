list_of_nums = eval(input("Enter a list of numbers: "))
ele_num = int(input("Enter a number to be linearly searched in the list: "))
for i in list_of_nums:  #performing a linear iteration with O(N) complexity
    if ele_num == i:  #searching with this linear iteration
        print("Number found in the list: ")
        break
else:
    print("Number not found in the list")
