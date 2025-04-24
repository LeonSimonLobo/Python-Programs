def main():
    import numpy as np
    num=int(input("Enter no. of strings:"))
    arrcenter=np.empty(0)
    arrleft=np.empty(0)
    arrright=np.empty(0)
    for i in range(num):
        string='abcdefghijklmnop'
        while len(string)>15:
            string=input("Enter string less than 15 characters:")
        arrcenter=np.append(arrcenter,np.char.center(string,15,'_'))
        arrleft=np.append(arrleft,np.char.ljust(string,15,'_'))
        arrright=np.append(arrright,np.char.rjust(string,15,'_'))
    print(arrcenter,arrleft,arrright,sep="\n")
if __name__=='__main__':
    main()