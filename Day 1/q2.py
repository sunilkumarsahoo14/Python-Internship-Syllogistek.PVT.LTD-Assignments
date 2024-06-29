# Calculate GCD Of Two Number

#define gcd function and with parameter a and b as num1 and num2
def gcd(a,b):  
    while(b):  
        a, a = b, a % b  
        return a 
     
#input firrst number
num1 = int(input ("Enter the first number: "))   

#input second number 
num2 = int(input ("Enter the second number: ")) 

 # call the gcd function with parse two parameter 
ans = gcd(num1, num2) 

print(f"The GCD Is: {ans}")