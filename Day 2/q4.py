# A Python program that takes a string and two indices as input and prints the substring between those indices.

# Taking input from the user
str = input("Enter the string: ")

#Take start and end index input
start_index = int(input("Enter Start Index: "))
end_index = int(input("Enter End Index: "))

# Find the substring from input string by string methods
sub_str = str[start_index-1:end_index]

# Print the answer string
print(f"Substring Is:{sub_str}")