#sum of all digits of a number

#defining the function
def sum(num):

    #if number is less than 10 than it is his sum
    if num < 10:
        return num
    
    #adding using recursion
    return num % 10 + sum(num//10)

#taking input
num=int(input("Enter the number "))

#storing the result
result=sum(num)

#displaying result
print(f"The sum of digits of {num} is {result}")