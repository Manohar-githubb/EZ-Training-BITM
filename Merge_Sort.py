def merge(l,low,mid,high):
    left=l[low:mid]
    right=l[mid+1:high]
    i=j=t=0
    temp=[0]*len(l)
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp[t]=left[i]
            i+=1
            t+=1
        else:
            temp[t]=left[j]
            j+=1
            t+=1
    while i<len(left):
        temp[t]=left[i]
        i+=1
        t+=1
    while j<len(right):
        temp[t]=right[j]
        j+=1
        t+=1
        
def merge_sort(l,low,high):
    if low<high:
        mid=low+(high-low)//2
        merge_sort(l,low,mid)
        merge_sort(l,mid+1,high)
        merge(l,low,mid,high)   
if __name__=="__main__":
    l=list(map(int,input().split()))
    merge_sort(l,0,len(l)-1)
    print("Sorted Array: ",l)