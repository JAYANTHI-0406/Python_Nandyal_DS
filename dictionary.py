# d1={'AP':'Amaravathi','Ap':'Guntur',2:4,8:64,2:16,'Nandayl':'Alagadda'}
# print(d1)
# print(type(d1)) # duplicates keys are not allowed in dictionary

student={"Name":"Jayanthi","Course":"BSC","Age":19,"Roll no":146}
# print(student)
# print(type(student))

# #Accessing Values

# print(student["Name"])
# print(student["Age"])
# print(student["Course"])
# print(student["Roll no"])

#some more methods in dict

#1.pop()
# student.pop("Name")
# print(studentt)

#2.popitem()
# student.popitem()
# print(student)

#3.key()
# print(student.keys())

# for i in student.keys():
#     print(i)

#4.values()
# print(student.values())

# for i in student.values():
#   print(i)

#5.item()
# print(student.items())

# for i in student.items():
#    print(i)

#6.get()
# print(student.get("Roll no"))

#7.update()
# print(student.update({"Name":"Pandu"}))
# print(student)

#9.clear()
# student.clear()
# print(student)

#10.copy()
# new_student=student.copy()
# print(new_student)

#11.setdefault()
# print(student.setdefault("city","Nandyal"))
# print(student)

#12.update()
# student["Age"]=19
# print(student)

# for i in range(10):
#     print(i,end=' ')

# for i in range(1,10,2):
#     print(i,end=" ")

# for i in range(2,10,2):
#     print(i,end=" ")

# for i in range(10,0,-2):
#     print(i,end=" ")

# for i in range(1,10,1):  
#     print(i,end=" ")

D1={'A':10,'B':30}
D2={'A':15, 'B':35}
result={}
for keys in D1:
    result[keys]=D1[keys]+D2[keys]
    print(result)

