l=[2,4,3,5,6,3,4,6,7,1,2,5]
window=max=0
k=int(input("Enter the no of continous digits: "))
for j in range(0,k):
    window+=l[j]
for i in range(0,len(l)-k):
    if max<window:
        max=window
        pos=i
    window=window+l[i+k]-l[i]
print(max)
for j in range(0,k):
    print(l[pos+j])