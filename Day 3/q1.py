# Find the number of alphabets in a string

#define function for no of alphabet count
def no_of_alphabet(str):
    # count variable used for counting
    count = 0
    # using for each loops for iteration operation
    for i in str:
        # string function isalpha() for checking alphabet or not
        if i.isalpha():
            # increment the count variable when condition meet
            count += 1
            # return the final count result
    return count

# taking input from the user
string = input("Enter String: ")

#print the final result with with function calling
print("The number of alphabets in the string is: ", no_of_alphabet(string))