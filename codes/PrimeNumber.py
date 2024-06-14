#Finding a prime number running within less time complexity.

n=int(input("Enter the number: "))
flag=0
if n<1:
    flag=1
elif n==1:
    flag=0
else:
    for i in range(2,(n//2)+1):
        if n%i==0:
            flag=1
            break
if flag==0:
    print("Valid prime Number")
else:
    print("Not a Prime Number")