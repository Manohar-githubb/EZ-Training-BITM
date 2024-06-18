L=list(map(int,input().split(" ")))
target=L[0]
for i in range(0,len(L)):
    if L[i]<target:
        target=L[i]
print(target)