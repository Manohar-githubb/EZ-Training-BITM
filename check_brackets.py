class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
e="[3+4]"
S=Stack()
ob="[({"
cb="])}"
flag=0
for i in e:
    if i in ob:
        S.push("[")
    if i in cb:
        x=S.pop()
        if x=="(" and i ==")":
            pass
        elif x=="{" and i =="}":
            pass
        if x=="[" and i =="]":
            pass
        else:
            flag = 1
            break
if flag==0 and S.size()==0:
    print("Valid")
if flag==1:
    print("Invalid")