# Write a program that can accept two strings as input and print the string with
# maximum length. If two strings have the same length, then the program
# should print both the strings line by line.

# define a function to do the task with parsing two parameter
def maximum_str_length(s1, s2):
    #checking the condition for s1 is long
    if len(s1) > len(s2):
        # condition meet then print s1
        print("The Maximum String Is:",s1)
        # if elif condition meet then s2 is long
    elif len(s1) < len(s2):
        # then print s2 
        print("The Maximum String Is:",s2)
    else: # for else condition -> same length then print all two string
        print(s1, s2)


# taking input from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Function calling
maximum_str_length(str1, str2)
