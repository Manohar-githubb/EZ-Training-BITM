#Code to move the zero values in the list to the end of the list
# i=0
# j=0
# ls1 = [4,0,5,0,1,9,0,0]
# for i in range(0,len(ls1)-1):
#     if ls1[i]!=0:
#         ls1[j]=ls1[i]
#         j=j+1
# while j<len(ls1):
#     ls1[j]=0
#     j=j+1
# print(ls1) 


#Factorial of a number
# n=5
# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(n))


#Power of a number using recursion
# n=int(input())
# m=int(input())
# def power(n,m):
#     if m==0:
#         return 1
#     else:
#         return n*power(n,m-1)
# result=power(n,m)
# print(result)


#Sum of digits of a number using recursion n=7654
# n=int(input())
# def sum(n):
#     if n<10:
#         return n
#     else:
#         return n%10 + sum(n//10)
# print(sum(n))

# class cse1:
#     def __init__(self,a,b):
#         self.a1=a
#         self.b1=b
#         print("I am construtor")
#     def strength(self):
#         print("The strength is 101")
#         self.s=101
#     def kn(self,c,d):
#         print("The knowledge is good")
#         self.know="Good"
#         pro=c+d
#         print(pro)
#     def details(self):
#         print("The current strength and the knowledge")
#         c_s=self.s-10
#         print(c_s,self.know)
#         print(self.a1+self.b1)
# day=cse1(20,30)
# print("From below is making function calls")
# day.strength()
# day.kn(2,10)
# day.details()

#Inheritance
# class Faculty:
#     def __init__(self,f_name,dpt,f_id):
#         self.f_name=f_name
#         self.dpt=dpt
#         self.f_id=f_id
#     def print_info(self):
#         print("Faculty information =",self.f_name,self.dpt,self.f_id)
# obj=Faculty("Ashish","Computer_Science",1001)
# obj.print_info()

# class CSE(Faculty):
#     pass
# obj1=CSE("Jyothi Mam","Computer_Science",1002)
# obj1.print_info()

#Multiple Inheritance
# class SubjMarks:
#     math = int(input("Enter paper marks of math"))
#     DE = int(input("Enter paper marks of design engineerim=ng"))
#     c = int(input("Enter paper marks of c language"))
#     english = int(input("Enter paper marks of english language"))
# class PractMarks:
#     cpract=int(input("Enter practical marks of c language"))
# class Result(SubjMarks,PractMarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40:
#             print

#converting into [0,0,0,1,1,1,2,2]
# ls=[2,1,0,1,1,2,0,0]
# count_0=0
# count_1=0
# count_2=0
# for i in range(len(ls)):
#     if ls[i]==0:
#         count_0 = count_0+1
#     elif ls[i]==1:
#         count_1+=1
#     else:
#         count_2+=1
# j=0
# while count_0>0:
#     ls[j]=0
#     j=j+1
#     count_0=count_0-1
# while count_1>0:
#     ls[j]=1
#     j=j+1
#     count_1=count_1-1
# while count_2>0:
#     ls[j]=2
#     j=j+1
#     count_2=count_2-1
# print(ls)


#OVERLOADING
#IN Python only "operator overloading" is possible, No method overloading and constructor overloading.
#OVERRIDING
#In Python both method and constructor overriding is possible. There is no concept of operator overriding here.

# class CarShowroom:
#     def CarCompany(self):
#         ls=['Mercedes','BMW']
#         while True:
#             choose_comp = input("Choose the car company: ")
#             if choose_comp in ls:
#                 print("Now you can select the model of the car.")
#                 self.CarModel()
#             else:
#                 print("Please re-enter the company.")
#     CarCompany()

#     def CarModel(self):
#         ls1=['E-class','C-class','X7','X5']
#         while True:
#             choose_model = input("Enter the car model: ")
#             if choose_model in ls1:
#                 print("Now You can select the variant of the car")
#             else:
#                 print("Re-enter the model again.")
    