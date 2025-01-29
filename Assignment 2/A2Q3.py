T=int(input("Enter no. of test cases:"))
N=[0]*T
for i in range(T):
    N[i]=int(input("Enter N:"))
divisors=[0]*len(N)
for i in range(len(N)):
    while N[i]>0:
        temp=N[i]
        digit=N[i]%10
        if not temp%digit:
            divisors[i]+=1
        N[i]//=10
for i in range(len(divisors)):
    print(divisors[i])

