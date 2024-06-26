def dp(p,w,c,DP,n):
    if c==0 or n==0:
        return 0
    for i in range(1,len(p)+1):
        for j in range(1,c+1):
            DP[i][c]=max(DP[i-1][c],p[i-1]+DP[i-1][c-w[i-1]])
    return DP

p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
c=15
n=len(p)
DP=[[0 for i in range(c+1)] for j in range(n+1)]
print(dp(p,w,c,DP,n))