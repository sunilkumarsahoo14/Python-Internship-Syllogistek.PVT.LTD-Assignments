#Q1.tofind the avg,min or max number
n=int(input("enter the number of elements:"))
l=[]
for i in range(0,n):
    l=l+[int(input("enter the element:"))]
#defination
def agnostic(l):
    l_min=min(l)
    l_max=max(l)
    avg=sum(l)/(l)
    #printing the result
    print("average:",avg)
    print("minimum:",l_min)
    print("maximum:",l_max)
agnostic(l)