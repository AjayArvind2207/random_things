arbit_input = input("Enter a string to check whether it is a palindrome: ").lower()  #lower makes it case insensitive
if arbit_input == arbit_input[::-1]:  #checks if string is same as reversed string
    print("This is a palindrome")
else:
    print("This is NOT a palindrome")
    
