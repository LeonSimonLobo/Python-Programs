num=int(input("Enter number:"))
temp=num
rev=0
if num<0:
    temp*=-1
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num<0:
    rev*=-1
print("The reversed number is",rev)
