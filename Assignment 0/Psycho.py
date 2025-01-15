N=int(input("Number of members:"))
count=0
members=[]
for i in range(N):
    temp=int(input(f"Height of team member {i+1}:"))
    members.append(temp)
for i in range(N):
    while members[i]!=i+1:
        temp=members[i]
        members[i]=members[temp-1]
        members[temp-1]=temp
        count+=1
print("The minimum number of swaps are:",count)