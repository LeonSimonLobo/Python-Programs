name=[]
for i in range(10):
    student=input("Enter name of student:")
    name.append(student)
for i in range(10):
    print(name[i][15::-1],end=' ')