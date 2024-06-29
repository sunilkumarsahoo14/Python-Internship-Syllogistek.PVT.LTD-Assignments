# A Python program that takes a string as input and prints the string in reverse using slicing.

#Taking input from user
str = input("Enter String: ")
    
# Reverse the string using slicing
# string[Start_point:stop_point:read]
rev_str = str[::-1]  # we not specify value so full string consider and -1 used for start from back side

# Printing the answer reverse string
print(f"The reversed string is: {rev_str}")