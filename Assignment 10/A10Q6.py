import numpy as np
import matplotlib.pyplot as plt
def get_valid_interval(f,max_iter=10000):
    while max_iter>0:
        a=np.random.uniform(-10,10)
        b=np.random.uniform(-10,10)
        if f(a)*f(b)<0:
            return a,b
        max_iter-=1
    return None,None
def bisection_method(f,a,b,tol=1e-6,max_iter=100):
    updates=[]
    for i in range(max_iter):
        c=(a+b)/2
        updates.append(c)
        if abs(f(c))<tol or abs(b-a)<tol:
            break
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        print(a,c,b)
    return np.array(updates)
def get_polynomial_function():
    expr=input("Enter a polynomial in terms of x: ")
    return lambda x:eval(expr)
def main():
    f=get_polynomial_function()
    a,b=get_valid_interval(f)
    if(a==None):
        print("Polynomial Function f does not change signs in (-10,10)")
        return
    print(f"Initial interval: a={a:.4f}, b={b:.4f}")
    updates=bisection_method(f,a,b)
    plt.plot(np.arange(len(updates)),updates)
    plt.xlabel('Iteration')
    plt.ylabel('Midpoint (Estimated Root)')
    plt.title('Bisection Method Root-Finding Process')
    plt.grid(True)
    plt.show()
if __name__=='__main__':
    main()
