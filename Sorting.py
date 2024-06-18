L=list(map(int,input().split(" ")))
i=0
for j in range(0,len(L)):
    for i in range(0,len(L)-1-j):
        if L[i]>L[i+1]:
            L[i],L[i+1]=L[i+1],L[i]
        else:
            i+=1
print(L)