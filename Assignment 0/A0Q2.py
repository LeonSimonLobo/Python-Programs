num=int(input("Enter number of which you want to find factorial:"))
while num<0:
    print("Inavlid number for factorial. It must be a whole number")
    num=int(input("Enter number of which you want to find factorial:"))
temp=num
fact=1
while temp>1:
    fact=fact*temp
    temp-=1
print(num,"!=",fact,sep='')