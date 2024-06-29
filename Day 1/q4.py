# Find Opposite Face Od The Dice Code In Python

# Function To 
def find_opp_face(face):
    #ensure face num is within valid range
    if 1 <= face <= 6:
        #calculate face
        return 7-face
    else: # if invalid condition then else part run
        return "Invalid Input!"
    
# Input From User
face_num = int(input("Enter Number: \n"))
# Calling Of find_opp_face Function
opposite_face = find_opp_face(face_num)
#print the output result with format string
print(f"{opposite_face}")