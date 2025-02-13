#calculate the number of prime number appears from 1 to n

#defining the function
def calculate(num):

    #if number is less than 1
    if num<=1:
        return False
    
    #if number is less than 3
    if num<=3:
        return True
    
    #if it is divisible by 2 or 3
    if num%2==0 or num %3==0:
        return False
    
    #checking 5 till the nth number
    i=5
    while(i*i<=num):
        if num%i==0 or num%(i+2)==0:
            return False
    i+=6
    return True

#defining the first function
def count(n):

    #for count
    c=0
    for num in range(2,n+1):

        #condition are true then increment
        if calculate(num):
            c+=1
    return c

#input
num=20

#calling/processing
result=count(num)

#output
print(result)