# import os
# with open("file.txt",'w') as f:
#     f.write(" Manohar")
#     f.close()
# with open("file.txt",'r') as f:
#     print(f.read())


#Replacing in files
# import os    
# with open("file.txt",'w') as f:
#     f.write("My name is Manohar\n")
#     f.write("I am currently in bellary\n")
#     f.write("I am taking super coder batch")
#     f.close()
# with open("file.txt",'r') as f:
#     s=f.read()
#     print(s)
#     f.close()
# s=s.replace("bellary","Bitm")
# print(s)

# SEEK usage
# with open("file.txt",'r') as f:
#     f.seek(10)
#     print(f.read())
#     f.close
    
# with open("file.txt",'rb') as f:
#     f.seek(-45,2)                      # 0 - For printing from there of the file, 1 - For printing from current location of the pointer, 2 - For printing from end of that file  
#     print(f.read().decode("utf-8"))
#     f.close

#for deletinf the file already created
# os.remove("file.txt")

with open("file2.txt",'wb') as f:
    eid=1
    name="bat"
    condition="good"
    s=f"{eid},{name},{condition}\n"
    f.write(s.encode())
    s=f"{eid},{name},{condition}\n"
    f.write(s.encode())
    f.close()
with open("file2.txt",'r') as f:
    s=f.read()
    print(s)
    f.close()