def digitroot(n):
    sum=10
    while sum>=10:
        sum=0
        while n>0:
            p=n%10
            sum+=p
            n//=10
        n=sum
    return sum
def main():
    n=int(input("Enter integer n:"))
    print("Digital root of",n,"is:",digitroot(n))
if __name__=='__main__':
    main()