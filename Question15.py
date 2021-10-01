first_list = eval(input("Enter a list"))
second_list = eval(input("Enter another list of the same size"))

'''
The concept behind this program is that since they have the same
number of elements, their corresponding indices have to be added
Hence, by simply finding the n'th element of both lists, we may
calculate the sum and get the required output.
Time Complexity --> O(N)
'''



sum_list = []

for i in range(len(first_list)):
    sum_list.append(first_list[i] + second_list[i])
print(sum_list)
