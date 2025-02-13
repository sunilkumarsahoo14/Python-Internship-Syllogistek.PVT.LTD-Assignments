#calculate the maximum item value that can be carried

#defining function for storing the value/weight
def calculate(item):
    return item[0]/item[1]

#defining function to calculate total value at which bag contain
def fractional(items,capacity):

    #storing the value/weight
    ratios=[]

    #calculate 
    for value,weight in items:
        ratio=calculate((value,weight))
        ratios.append((ratio,value,weight))

        #sort the list
    ratios.sort(reverse=True,key=calculate)

    #calculate capacity of a bag
    total=0.0
    remaining=capacity

    #store the items
    for ratio,value,weight in ratios:

        #if overflow or complete the capacity
        if remaining<=0:
            break
        #space is remaining
        if weight <= remaining:
            total+=value
            remaining-=weight
        else:
            total+=ratio*remaining
            remaining=0
    return total

#taking input
item=[(60,10),(100,20),(120,30)]
capacity=50

#calling function and storing function
max=fractional(item,capacity)

#printing result
print(max)