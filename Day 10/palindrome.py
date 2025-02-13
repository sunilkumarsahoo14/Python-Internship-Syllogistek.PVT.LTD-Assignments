#wap that the word is palindrome or not

#defing the function
def palindrome(str):

    #if one word or 0 word is present on string
    if len(str) <=1:
        return True
    
    #if first and last elment are not equal
    if str[0]!=str[-1]:
        return False
    
    #if first and last are equal then get on next one and last 2 and so on
    return palindrome(str[1:-1])

#taking input
str=input("Enter the string ")

#storing the result
result=palindrome(str)

#printing the result
print(result)