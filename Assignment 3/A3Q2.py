def IsFibo(n):
    fib0=0
    if n==0:
        return 'IsFibo'
    fib=1
    while fib<=n:
        if n==fib:
            return 'IsFibo'
        temp=fib
        fib+=fib0
        fib0=temp
    return 'IsNotFibo'
def main():
    T=int(input("Enter no. of test cases:"))
    tests=[]
    while T>0:
        test=int(input("Enter number:"))
        tests.append(test)
        T-=1
    for i in range(len(tests)):
        print(IsFibo(tests[i]))
if __name__=='__main__':
    main()