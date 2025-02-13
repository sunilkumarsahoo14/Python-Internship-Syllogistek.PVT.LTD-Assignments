#wap to check if two string are anagram of each other or not

#defining function
def anagram(str1,str2):

    #removing space and converting all lower case
    str1=str1.lower().replace(" ","")
    str2=str2.lower().replace(" ","")

    #if length din't match then return false
    if len(str1)!=len(str2):
        return False
    
    #making dictionary to store both the letter of string
    count1={}
    count2={}

    #storing the letter in first dic
    for char in str1:
        if char in count1:
            count1[char]+=1
        else:
            count1[char]=1

    #storing the letter in sec dic
    for char in str2:
        if char in count2:
            count2[char]+=1
        else:
            count2[char]=1

        #giving the result by comparing the dic weather the they are equal or not
    return count1==count2

#taking inut
str1="Listen"
str2="Silent"

#calling the function and storing the result
result=anagram(str1,str2)

#output
print(result)