list_of_nums = eval(input("Enter a list of numbers"))
sum_d = 0
list_acc = []
for number in list_of_nums:   #iterating through the list of digits
    sum_d = 0
    for digit in str(number): 
        sum_d+=int(digit)**3   #calculating cube of digits to check armstrong
    if sum_d == number:
        print("Condition is satisfied for number", number)
        list_acc.append(number)
print("Smallest number satisfying the condition =",min(list_acc), "and maximum number =", max(list_acc))
    
        
