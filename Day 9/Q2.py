#Q2.to find the row index of the char present in the matrix
mat=[[],[],[]]
row=int(input("enter the num of rows:"))
col=int(input("enter the num of columns:"))
ch=input("enter the char to be searched:")
for i in range(row):
    for j in range(col):
        mat[i].append(input("enter the element"))
found=False
def search(mat,ch):
    #condition for searching
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(mat[i][j]==ch):
                print(f"the character {ch} is present in the matrix at index",i,j)
                found=True
if found==False:
    print(f"the char {ch} is not present in the matrix")
search(mat,ch)