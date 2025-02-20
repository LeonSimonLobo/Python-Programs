def next_permutation(w):
    w=list(w)
    i=len(w)-2
    while i>=0 and w[i]>=w[i+1]:
        i-=1
    if i==-1:
        return "no answer" 
    j=len(w)-1
    while w[j]<=w[i]:
        j-=1
    w[i],w[j]=w[j],w[i]
    w=w[:i+1]+w[i+1:][::-1]
    return "".join(w)
def main():
    T=int(input("Enter no. of test cases:"))
    results=[]
    for i in range(T):
        w=input("Enter string:")
        results.append(next_permutation(w))
    print("\n".join(results) + "\n")
if __name__=='__main__':
    main()