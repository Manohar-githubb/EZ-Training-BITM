# ls=[int(x) for x in input("Enter the number to choose candidate ").split()]
# print(ls)
# count=0
# i=0
# j=1
# for i in range(0,len(ls)-1):
#     if ls[i]==j:
#         count=count+1
#         j=j+1
#     else:
#         i=i+1
# print(count)

vote=list(map(int,input("Enter the voters: ").split()))
count=[0]*6
for i in vote:
    count[i-1]=count[i-1]+1
    print(i,count)
print("Final count=",count)