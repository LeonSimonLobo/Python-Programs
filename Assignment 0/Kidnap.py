T=int(input("Number of test cases:"))
while T>100 or T<1:
    print("Number of test cases must be between 1 and 100")
    T=int(input("Number of test cases:"))
while T>0:
    N=int(input("Number of boxes:"))
    while N>105 or N<2:
        print("Number of boxes must be between 2 and 105")
        N=int(input("Number of boxes:"))
    X=int(input("Box in which coin is kept:"))
    while X>N or X<1:
        print("Box must be between 1 and",N)
        X=int(input("Box in which coin is kept:"))
    S=int(input("Number of swaps:"))
    while (S>104 or S<1) or S*T>1025:
        print("Number of swaps must be between 1 and 104")
        S=int(input("Number of swaps:"))
    while S>0:
        A=int(input("First box to swap:"))
        while A>N or A<1:
            print("Box must be between 1 and",N)
            A=int(input("First box to swap:"))
        B=int(input("Second box to swap:"))
        while B>N or B<1:
            print("Box must be between 1 and",N)
            B=int(input("Second box to swap:"))
        if A==X:
            X=B
        elif B==X:
            X=A
        S-=1
    T-=1
print("The gold coin is in box",X)