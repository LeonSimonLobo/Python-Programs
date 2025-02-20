def main():
    T=int(input("Enter no. of test cases:"))
    while T<1 or T>10:
        T=int(input("No. of test cases must be greater than 0 and less than 11. Please enter again:"))
    cuts=[]
    pieces=[]
    for i in range(T):
        cuts.append(int(input("Enter no. of cuts:")))
        temp=cuts[i]//2
        pieces.append((cuts[i]-temp)*temp)
    for i in range(len(pieces)):
        print("Maximum no. of pieces of chocolate in",cuts[i],"cuts is",pieces[i])
if __name__=='__main__':
    main()