
#define a function takes a list items as input and removes duplicates while preserving the original order of elements.
def remove_duplicates(items):
    #This seen is a set that keeps track of elements that have already been encountered
    seen = set()
    #This result list stores the elements in the order they are encountered without duplicates
    result = []
    #It iterates through each item in the items list
    #For each item, it checks if item is not already in the seen set or not
    for item in items:
        #If the item not in seen it adds item to both the seen set and the result list.
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

#user enter a list by comma-separated list of elements.
list = input("Enter comma-separated list of elements: ")
#split method is used to split the string stored in list into a list of elements
items = list.split(',')

#his line calls a hypothetical function remove_duplicates with items as an argument
new_list = remove_duplicates(items)
print("List after removing duplicates with original order preserved: ")
print(','.join(new_list))

#output
""" Enter comma-separated list of elements: apple,banana,orange,apple,mango,banana
List after removing duplicates with original order preserved: 
apple,banana,orange,mango"""