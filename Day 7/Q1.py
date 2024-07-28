#Q1. Given two strings find the longest common prefix for them
def longest_common(str1,str2):
    prefix=""
    #find the min length btw the 2 strings
    min_len=min(len(str1),len(str2))
    #iterate charecters
    for i in range(min_len):
        if str1[i]==str2[i]:
            prefix+=str[i]
        else:
            break
        return prefix
    input1="flower"
    input2="flow"
    res=longest_common(input1,input2)
    #print the result
    print(res)
