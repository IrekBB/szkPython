def fib(x):
    if (x<2):
        return x
    else:
        return fib(x-1) + fib(x-2)

def fib_dyn(n):
    if n <= 2:
        return [0, 1]
    fTab  = [0] * (n+1) #Tablica na wyniki
    fTab[1] = 1
    for i in range (2, n+1):
        fTab[i] = fTab[i-1] + fTab[i-2]
    return fTab

def  main(args):
    N = 12
    f = fib_dyn(N)
    print(f)
    print("Wyniki:")
    for i in range(N+1):
        print(f"fib({i:2})={f[i]:>10} \t metoda klasyczna: {fib(i):>10}")


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

    
