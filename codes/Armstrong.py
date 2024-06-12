num=int(input())
num1=num
count=0
ans=0
org=num1
while num>0:
    count+=1
    num=num//10
while num1>0:
    digit=num1%10
    p=digit**count
    ans=ans+p
    num1=num1//10
if ans==org:
    print("Armstrong")
else:
    print("No")