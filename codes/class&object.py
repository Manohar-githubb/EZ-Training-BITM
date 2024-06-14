# class Student:
#     def __init__(self,nm,ag,gn):
#         self.name=nm
#         self.age=ag
#         self.gender=gn
#         self.branch="CSE"
# s1=Student("Manu",20,"Male")
# print(s1.name)
# print(s1.branch)

# class Student:
#     def __init__(self,nm,ag,gn):
#         self.name=nm
#         self.age=ag
#         self.gender=gn
    
# a=input("Enter the name: ")
# b=input("Enter the age: ")
# c=input("Enter the gender: ")

# s1=Student(a,b,c)
# print(s1.name,s1.age,s1.gender)
# s1.age=21
# print(s1.name,s1.age,s1.gender)


# class Std:
#     def __init__(self):
#         self.USN=None
#         self.Name=None
#         self.Marks=[]
#         self.Percentage=None
#         self.grade=None
#     def Std_input(self):
#         self.Name=input("Name: ")
#         self.USN=input("USN: ")
#         for i in range(0,5):
#             Marks=int(input(f"Marks for {i+1}: "))
#             self.Marks.append(Marks)
#     def calc_percentage(self):
#         sum=0
#         for i in self.Marks:
#             sum+=i
#         self.Percentage=(sum/500)*100
#     def calc_grade(self):
#         per=self.Percentage
#         if per>=90:
#             self.grade="A"
#         elif per>=80:
#             self.grade="B"
#         elif per>=70:
#             self.grade="C"
#         elif per>=60:
#             self.grade="D"
#         else:
#             self.grade="Invalid"
#     def print_details(self):
#         print("Name: ",self.Name)
#         print("USN: ",self.USN)
#         print("Marks: ")
#         for i in range(0,5):
#             print(f"Marks of subject {i+1} is ", self.Marks[i])
#         print("Percentage: ",self.Percentage)
#         print("Grade: ",self.grade)
        

# obj=Std()
# obj.Std_input()
# obj.calc_percentage()
# obj.calc_grade()
# obj.print_details()

            
class Std:
    
    def __init__(self): 
        self.__USN = None
        self.__Name = None
        self.__Marks = []
        self.__Percentage = None
        self.__Grade = None

    def Std_Input(self):
        self.__Name = input("Enter your Name: ")
        self.__USN = input("Enter Your USN: ")
        for i in range (0,5):
            marks = input(f"Enter Your Marks in Sub{i+1} : ")
            self.__Marks.append(marks)

    def calc_percentage (self):
        sum = 0
        for i in self.__Marks:
            sum = sum + int(i)
        self.__Percentage = (sum/500)*100

    def calc_Grade(self):
        per = float(self.__Percentage)
        if per<=100 and per >=80:
            self.__Grade = "A"
        elif per<80 and per >=60:
            self.__Grade = "B"
        elif per<60 and per >=40:
            self.__Grade = "C"
        elif per<40 and per >=0:
            self.__Grade = "D"
        else: 
            self.__Grade = "Inavlid"

    def print_details(self):
        print("Name: ",self.__Name)
        print("USN : ",self.__USN)
        print("Marks in Five Subject are :")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.__Marks[i]}")
        print("Percentage : ", self.__Percentage)
        print("Grade : ", self.__Grade)

    def convert_list(self):
        st_list = [self.__USN,self.__Name,self.__Marks,self.__Percentage,self.__Grade]
        return st_list

    def covert_ob(self,stu_list):
        self.__USN = stu_list[0]
        self.__Name = stu_list[1]
        self.__Marks = stu_list[2]
        self.__Percentage = stu_list[3]
        self.__Grade = stu_list[4]

st1 = Std()
print(type(st1))
st1.Std_Input()
st1.calc_percentage()
st1.calc_Grade()
st1.print_details()

with open("student.txt",'wb') as File:
    L=st1.convert_list()
    data = f"{L[0]}|{L[1]}|{L[2][0]},{L[2][1]},{L[2][2]},{L[2][3]},{L[2][4]}|{L[3]}|{L[4]}\n"
    File.write(data.encode())
    File.close()
stu_list=[]

with open("student.txt",'rb') as File:
    data = File.readline().decode('utf-8')
    print(data)
    for i in data.split("|"):
        stu_list.append(i)
    mrks=stu_list[2]
    mrks_list = []
    for i in mrks.split(','):
        mrks_list.append(i)
    stu_list[2]=mrks_list

print(stu_list)
st2=Std()
st2.covert_ob(stu_list)
st2.print_details()