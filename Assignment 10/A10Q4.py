def main():
    import numpy as np
    N=int(input("Enter N:"))
    arr=np.random.uniform(low=-100,high=100,size=(N,2))
    polar_arr=np.random.uniform(low=-100,high=100,size=(N,2))
    x=arr[:,0]
    y=arr[:,1]
    mag=np.sqrt(x**2+y**2)
    theta=np.arctan2(y,x)
    polar_arr=np.column_stack((mag,theta))
    print(np.array2string(arr,separator=","))
    print(np.array2string(polar_arr,separator=","))
if __name__=='__main__':
    main()
