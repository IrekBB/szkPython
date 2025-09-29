def fib_i(n):
    a,b=0,1
    L=[]
    for i in range(n):
        L.append(b)
        b=b+a  # następny wyraz ciagu fib: a + b
        a=b-a  # wyraz n-1: pod zmienną a przypisujemy wartość zmiennej b
    return L

def fib_r(n):
    if n<3:
        return 1
    return fib_r(n-2)+fib_r(n-1) 

print (fib_r(5))
