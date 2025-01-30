def utopiantree(N):
    height=1
    for i in range(1,N+1):
        if i%2:
            height*=2
        else:
            height+=1
    return height
def main():
    T=int(input("Enter no. of test case:"))
    while T>10 or T<1:
        T=int(input("Number of test cases must be between 1 and 10. Please enter again:"))
    cases=[]
    for i in range(T):
        test=int(input(f"Enter no.of cycles in test case {i+1}:"))
        while test>50 or test<0:
            test=int(input("Number of cycles must be between 0 and 50. Please enter again:"))   
        cases.append(test)
    for i in cases:
        print("The height of the tree after",i,"cycles is:",utopiantree(i))
if __name__=='__main__':
    main()