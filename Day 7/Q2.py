#Q2.calculate speed
def calculate_speed(dist,time):
    #using list comprehension to calculate speed
    speed=[dist[i]/time[i] if time[i] !=0 else 0 for i in range(min(len(dist),len(time)))]
    return speed
#taking input
dist=[10,20,30,40,50]
time=[1,5,3,2,4]
#print result
s=calculate_speed(dist,time)
print(f"speed:{s}")
