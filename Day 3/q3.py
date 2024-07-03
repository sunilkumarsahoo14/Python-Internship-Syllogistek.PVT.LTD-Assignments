# Write a program to find Leap year.

# Function for leap year find
def leapyear(year):
    
    if year % 4 == 0:
        # Check if the year is evenly divisible by 100
        if year % 100 == 0:
            # Check if the year is evenly divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# input from the user
year = int(input("Enter a year: "))

# if the year is a leap year
if leapyear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
