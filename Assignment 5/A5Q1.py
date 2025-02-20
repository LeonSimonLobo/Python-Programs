def main():
    L=int(input("Enter lower bound:"))
    R=int(input("Enter higher bound:"))
    while L<1 or L>1000:
        L=int(input("Lower bound must be greater than 0 and less than 1000. Please enter again:"))
    while R<1 or R>1000 or R<L:
        R=int(input("Higher bound must be greater than 0 and less than 1000 and greater than lower bound. Please enter again:"))
    xor=L^R
    expo=1
    while expo<=xor:
        expo*=2
    print(expo-1)
if __name__=='__main__':
    main()
