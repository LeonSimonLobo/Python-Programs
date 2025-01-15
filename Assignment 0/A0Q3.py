num=int(input("Enter number of which you want to calculate factorial:"))
while num<0:
    print("Inavlid number for factorial. It must be a whole number")
    num=int(input("Enter number of which you want to calculate factorial:"))
fact=1
while num>1:
    fact=fact*num
    num-=1
print("Factorial of given number=",fact,sep='')