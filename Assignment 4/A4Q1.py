def main():
    minopp=[]
    T=int(input("Enter no. of test cases:"))
    while T<1 or T>10:
        T=int(input("Number of test cases must be between 1 and 10. Please enter again:"))
    while T>0:
        opp=0
        st=input("Enter string:")
        st=st.lower()
        for i in range(len(st)//2):
            opp+=abs(ord(st[i])-ord(st[len(st)-1-i]))
        minopp.append(opp)
        T-=1
    for i in minopp:
        print("Minimum no. of operations is",i)
if __name__=='__main__':
    main()