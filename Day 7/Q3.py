#Q3.validity check
def is_valid_triangle(a, b, c):
    #Check if the given sides form a valid triangle
    return a + b > c and b + c > a and c + a > b

def classify_triangle(a, b, c):
    #Classifing the triangle based on its sides
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or c == a:
        return "Isosceles"
    else:
        return "Scalene"

def circumcenter_radius(a, b, c):
    #Calculate the radius of circumcenter (if right-angled)
    if is_valid_triangle(a, b, c):
        # Calculate semi-perimeter
        s = (a + b + c) / 2
        # Calculate area using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        # Calculate circumradius
        circumradius = (a * b * c) / (4 * area)
        return circumradius if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 else -1
    else:
        return -1

# taking input
a = float(input("Enter side 'a': "))
b = float(input("Enter side 'b': "))
c = float(input("Enter side 'c': "))

if is_valid_triangle(a, b, c):
    triangle_type = classify_triangle(a, b, c)
    print(f"The triangle is {triangle_type}.")
    circumcenter_rad = circumcenter_radius(a, b, c)
    if circumcenter_rad != -1:
        print(f"Circumcenter radius: {circumcenter_rad:.2f}")
    else:
        print("The triangle is not right-angled.")
else:
    print("Invalid sides. Cannot form a triangle.")

