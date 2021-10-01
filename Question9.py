string_count = input("Enter a string: ")
counter_dict = {}   #serves as the dictionary where the counting will take place

'''
Part 1:
Dictionary unique string counter
'''

for i in string_count:
    if i not in counter_dict:
        counter_dict[i] = 1
    else:
        counter_dict[i]+=1
print("Counter dictionary is:\n",counter_dict)


'''
Part 2:
Employee details characterization'''


employee_details = {}

while True:    #using an infinite loop
    empl = input("Enter employee's name (Enter to quit) ")
    if empl == '':
        break
    salary = float(input("Enter employee's salary: "))  
    employee_details[empl] = salary
    #Here is where the appending happens

print("Employee details of the company are:",employee_details)
