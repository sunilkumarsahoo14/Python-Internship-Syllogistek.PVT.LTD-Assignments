#Defines a function named largest_number that takes two parameters: A for list of numbers and n is the position of the largest number to find).


def largest_number(A, n):
    # Sort the list in descending order
    A.sort(reverse=True)
    # Return the nth largest number
    return A[n - 1]

# take user input for the list
l1= input("Enter a comma-separated list of numbers: ")
# Convert the input string to a list of integers
A = list(map(int, l1.split(',')))

# take nth input value from the user 
n = int(input("Enter the value of n: "))

# display with function calling the nth largest number
print(f"The {n}rd largest number is {largest_number(A, n)}.")

#output
""" Enter a comma-separated list of numbers: 10, 5, 20, 8, 15
Enter the value of n: 2
The 2rd largest number is 15
or
Enter a comma-separated list of numbers: 2,5,7,1,9
Enter the value of n: 3
The 3rd largest number is 5. """