# Program to find consonants in a string

# definne a function
def consonants(str):

    # Empty string 
    consonant = ""

    # for each loop 
    for i in str:

        # Check for the character is vowel or not ---> if not vowel then execute next 
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U': 

            #if not vowel and alphabet then execute next 
            if i.isalpha():

                # if condition meet then store the string in previously defined string
                consonant += i
                # finally return the answer string
    return consonant

# Take Input from the user
user_input = input("Enter a string: ")

# Finding consonants by function call
final_consonants = consonants(user_input)

# Printing the result consonants string
print("Consonants in the string are:", final_consonants)