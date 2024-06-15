list=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
for i in range(0,len(list)-2):
    sum=list[i]+list[i+1]+list[i+2]
    if max<sum:
        max=sum
        pos=i
print(max,list[pos],list[pos+1],list[pos+2])