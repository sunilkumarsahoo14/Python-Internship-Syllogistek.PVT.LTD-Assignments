# Find if the sub-string exists in the string without using in operator
# Taking  the main string and the substring input from the user

string = input("Please enter the main string: ")
substring = input("Please enter the substring to check: ")

# Check if the substring exists in the main string using find method
#The find method of the string object is used here and this find method searches for the substring within the main string.
#If the substring is found, find returns the index of the first occurrence of the substring within the main string.
#If the substring is not found, find returns -1.

#If the substring is found then line prints a message indicating that the substring is present in the main string.

if string.find(substring) != -1:
    print(f"The substring '{substring}' is present in the string.")

#If the substring is not found and this line prints a message indicating that the substring is not present in the main string.
else:
    print(f"The substring '{substring}' is not present in the string.")

#output
""" Please enter the main string: Hello world
Please enter the substring to check: world
The substring 'world' is present in the string.
or
Please enter the main string: hello abani 
Please enter the substring to check: world
The substring 'world' is not present in the string.
"""