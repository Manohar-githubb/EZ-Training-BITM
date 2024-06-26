p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
p_w={}
for i in range(len(p)):
    p_w[i]=p[i]/w[i]
l=list(p_w.items())
sorted_list=sorted(l,key=lambda x: x[1],reverse=True)
print(sorted_list)
l.sort(key=lambda x: x[1],reverse=True)
print(l)