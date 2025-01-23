import random
list=[]
count=0
max=0
for i in range(100):
    list.append(random.randint(0,1))
    if list[i]==1:
        if count>max:
            max=count
        count=0
    else:
        count+=1
print(list)
print(max)