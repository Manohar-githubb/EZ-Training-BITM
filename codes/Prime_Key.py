# Level 1: Find the smallest prime number larger than a given integer N.
# Level 2: Calculate the sum of all numbers between N and the smallest 
# prime number larger than N.
# Level 3: Determine if the product of the smallest prime number larger than N
# and the next immediate prime number is also a prime.

def check_prime(n):
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
        return 1
    else:
        return 0
    
result=[]
N=int(input("Enter the Prime Key: "))
flag=0
k=N+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        result.append(k)
    else:
        k=k+1
        
sum=0
for i in range(N+1,k):
    sum+=i
result.append(sum)

p1=k
flag=0
k=p1+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1

p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)
print(f"The next smallest prime number is {result[0]}")
print(f"The sum of numbers between N and next smallest prime number = {result[1]}")
print(f"Thus the product of next prime numbers are true or false?...{result[2]}")
#converting the list into a tuple.
prime_key=tuple(result)
print(prime_key)