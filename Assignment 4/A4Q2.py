def main():
    import math
    squares=[]
    T=int(input("Enter no. of test cases:"))
    while T<1 or T>100:
        T=int(input("Number of test cases must be between 1 and 10. Please enter again:"))
    while T>0:
        A,B=input("Enter lower limit and upper limit:").split()
        A=int(A)
        B=int(B)
        while B<A:
            B=int(input("Upper limit must be greater than lower limit. Please enter again:"))
        lower=int(math.sqrt(A))
        if math.sqrt(A)==lower:
            lower-=1
        higher=int(math.sqrt(B))
        squares.append(higher-lower)
        T-=1
    for i in squares:
        print("No. of squares are:",i)
if __name__=='__main__':
    main()