#count the targeted value present in the array

#defining the function
def binary_search(array,target):

    #binary search logic
    low=0
    high=len(array)-1
    while(low<=high):
        mid=(low+high)//2
        if (array[mid]==target):

            #counting how many targeted value are there
            position=search(array,mid,target)
            return(position)
        
        #if not found then changing the array index postion bases of the value
        elif array[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return 0

#counting how many targeted value are there
def search(array,mid,target):
    #taking start and end index
    num1=mid
    num2=mid

    #finding starting index
    while(array[num1-1]==target):
        num1-=1

    #finding ending index
    while(array[num2+1]==target):        
        num2+=1
    #counting
    return(num2-num1)+1

#taking input
list=[1,4,4,4,4,4,4,4,4,5]
target=4

#calling the function and storing the result
result=binary_search(list,target)

#showing the result
print(result)