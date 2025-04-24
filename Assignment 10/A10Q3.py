def main():
    import numpy as np
    N=int(input("Enter N:"))
    val=(N**2+1)//2
    arr=np.zeros((N,N))
    arr=arr+val
    if not N%2:
        for i in range(N):
            k=i%2
            for j in range((N//2)*k,(N//2)*k+N//2):
                arr[i][j]+=1
    print(arr)
if __name__=='__main__':
    main()