"""
Write a program that accepts a sentence and calculate the number of letters 
and digits. Example: Suppose the following input is supplied to the program: 
hello world! 123! Then, the output should be: LETTERS 10 DIGITS 3
"""

# function definatio 
def count_ltr_dgt(sentence):

    # define two variables for letters and digits
    letters = 0
    digits = 0

    # taking a loops for iterating the values
    for i in sentence:
        # condition match then increment letters
        if i.isalpha():
            letters += 1
        # condition match then incremet digits
        elif i.isdigit():
            digits += 1
            # return the two values
    return letters, digits

# user inputs taking
input_str = input("Enter The Sentence: ")

# Calling the function
letters, digits = count_ltr_dgt(input_str)

# print the results
print("No Of Letters:", letters)
print("No Of Digits:", digits)