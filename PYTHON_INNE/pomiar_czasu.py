def silnia(n):
    if n==0:
        return 1
    else:
        return n * silnia(n-1)

def silnia_it(n, res=1):
    while n!=0:
        res = n * res
        n = n - 1
    return res

def silnia_z_param_dodat(n, tmp=1):
    if n==0:
        return tmp
    else:
        return silnia_z_param_dodat(n-1, n*tmp)

def main(args):
    while True:
        try:
            n = int (input("Podaj n:"))
            break
        except ValueError:
             print("Oops!  To nie liczba.  Spróbuj ponownie...")
        
    czasstart = time.time()
    wynik = silnia(n)
    czasend = time.time()
    print ("------------ Funkacja klasyczna silnia -----------")
    print (f"Czas start:{czasstart:20}, czas end={czasend}")
    print (f"Silnia z {n} rekurencyjnie: {wynik}, czas: {czasend-czasstart}s")
    
    print()
    
    czasstart = time.time()
    wynik = silnia_z_param_dodat(n)
    czasend = time.time()
    print ("------------ Funkacja silnia z parametrem dodatkowym -----------")
    print (f"Czas start:{czasstart:20}, czas end={czasend}")
    print (f"Silnia z {n} rekurencja z parametrem dodatkowym: {wynik}, czas: {czasend-czasstart}s")

    print()

    czasstart = time.time()
    wynik = silnia_it(n)
    czasend = time.time()
    print ("------------ Funkacja silnia w wersji iteracyjnej -----------")
    print (f"Czas start:{czasstart:20}, czas end={czasend}")
    print (f"Silnia z {n} iteracyjnie: {wynik}, czas: {czasend-czasstart}s")


    
    
if __name__=="__main__":
    import sys
    import time
    sys.exit(main(sys.argv))
    
