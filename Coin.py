l=[1,5,7]
l.sort(reverse=True)
b=18
i=0
min_count=0
while b>0:
    if b>=l[i] and i<len(l):
        min_count+=1
        b=b-l[i]
    else:
        i+=1
print(f"Minimum Coins = {min_count}")