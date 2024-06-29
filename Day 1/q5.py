# Python code to calculate distance between two points

# import math 
import math

#function to calculate distance between two points
def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #formula to calculate distance

#taking input from user for point - 1
x1 = float(input("Enter the x-coordinate of point 1: "))
y1 = float(input("Enter the y-coordinate of point 1: "))

#taking input from user for point - 2
x2 = float(input("Enter the x-coordinate of point 2: "))
y2 = float(input("Enter the y-coordinate of point 2: "))

# function calling for calculating distance 
distance = calc_distance(x1,y1,x2,y2)

#printing the result
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")