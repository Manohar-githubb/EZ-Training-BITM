ctr=[0]
def tower (n,frm,aux,to):
    if n==0:
        return
    tower(n-1,frm,aux,to)
    ctr[0]+=1
    print(f"Move {n} from {frm} to {to}")
    tower(n-1,aux,to,frm)
n=2
ctr=[0]
tower(n,'A','B','C')
print(ctr)