# def print_num(n):
#     if n<10:
#         print_num(n+1)
#         print(n)
#     return
# print_num(0)

# Fibanocci Series
t=[0]
def fib(n):
    t[0]+=1              
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1)+fib(n-2)

if __name__=="__main__":
    n=int(input())
    print(fib(n))
    print(t)                     #Time Complexity