# Program to add two matrix

# first matrix
mat1 = [[1,2,3],[1,2,3],[1,2,3]]

# second matrix
mat2 = [[1,2,3],[1,2,3],[1,2,3]]

# Answer matrix
mat3 = [[0,0,0],[0,0,0],[0,0,0]]

# Travel by rows
for i in range(len(mat1)):
    
   # travel by columns
   for j in range(len(mat1[0])):
       # adding the two matrix and store it in matrix 3
       mat3[i][j] = mat1[i][j] + mat2[i][j]

# printing result matrix
for i in mat3:
   print(i)



