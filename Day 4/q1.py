# Check string is palindrome or not 

# Function to check palindrome
def palindrome(str):

    # string reversing and returning true if equals 
    result = (str == str[::-1])

    # return result
    return result

# Taking string user input
string = input("Enter String: ")

# Clling palindrome function
check_palin = palindrome(string) # Return True Or False 

# Print result with check the true or false with if condition
if check_palin:
    # Print for true
    print("String is palindrome")
else:
    # Print for false
    print("String is not palindrome")
