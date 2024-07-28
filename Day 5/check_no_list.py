#Find if a number is present in a list. 
# Get list input from the user
list = input("Enter a list of numbers separated by spaces: ")

# Split the input string and manually convert each item to an integer
my_list = []

# iterate the for loop for to convert type cast for integer and add to the list
for item in list.split():
    my_list.append(int(item))

# Get the number to check from the user
check_no = int(input("Enter a number to check: "))

# if check the number is in the list or not
#if exit then print the number
if check_no in my_list:
    print(f"{check_no} is in the list.")
# if the no does not exit then print false statement
else:
    print(f"{check_no} is not in the list.")

#output
""" Enter a list of numbers separated by spaces: 1 2 3 4 5
Enter a number to check: 3
3 is in the list. """