# Check A number is a perfect square or not

#importing the math module
import math

# Function definatin for perfect square checking
def perfect_sqr(num):

    if num < 0:
        # For negative no it is false return
        return False 
    
    # otherwise execute the next part that find square root of given number

    # sqrt store the square root of  num 
    sqrt = math.sqrt(num)

    # check the the number with the square rotted numbers square
    check = (sqrt * sqrt == num)

    # return the check for true & false
    return check

# Input from the user
usr_num = int(input("Enter number: "))

# Check if the input number is a perfect square and print the results as per conditions
if perfect_sqr(usr_num):
    print("Number is perfect square.")
else:
    print("Number is not perfect square.")
