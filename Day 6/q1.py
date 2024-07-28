"""
 Write a program to solve a classic ancient Chinese puzzle: We count 35 
heads and 94 legs among the chickens and rabbits in a farm. How many 
rabbits and how many chickens do we have? Hint: Use for loop to iterate all 
possible solutions.
"""

def chicken_rabbit(total_heads, total_legs):

    for rabbits in range(total_heads + 1):

        chickens = (total_heads - rabbits)
        all_legs = (2 * chickens) + (4 * rabbits)

        if all_legs == total_legs:

            return chickens, rabbits

total_heads = int(input("Enter Total Heads: "))
total_legs = int(input("Enter Total Legs: "))

chicken, rabbit = chicken_rabbit(total_heads, total_legs)

if chicken:

    print("Chickens:", chicken)
    print("Rabbits:", rabbit)