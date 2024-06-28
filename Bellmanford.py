# D={
#   0:[(0,1,6),(0,2,4),(0,3,5)],
#   1:[(1,4,-1)],
#   2:[(2,1,-2),(2,4,3)],
#   3:[(3,2,-2),(3,5,-1)],
#   4:[(4,5,3)],
#   5:[]
# }

G=[
    [0,6,4,5,False,False],
    [False,0,False,False,-1,False],
    [False,-2,0,False,3,False],
    [False,False,-2,0,False,-1],
    [False,False,False,False,0,3],
    [False,False,False,False,False,0]
]

d={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F"}
E_L=[]
for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j]!=False and G[i][j]!=0:
            E_L.append(tuple((i,j)))
print(E_L)

dist={i:float('inf') for i in d}
dist[0]=0
print(dist)

# for i in range(len(G)-1):
for i in G:
    for j in E_L:
        new_dist=dist[j[0]]+G[j[0]][j[1]]
        if dist[j[1]]>new_dist:
            dist[j[1]]=new_dist
print(dist)