def szukaj(tabl, left, right, x):
    if left> right:
        print (f"Element: {x} nie został znaleziony")
    else:
        if tabl[left] == x :
            print (f"Element: {x} został znaleziony")
        else:
            szukaj(tabl, left+1, right, x)


def silnia(x):
    if x==0:
        return 1
    else:
        return x * silnia(x-1)

def fib(x):
    if x<2:
        return x
    else:
        return fib(x-1)+fib(x-2)

def main(args):
    print ("************** SZUKAJ **************")
    tabl=[1,2,3,2,-7,44,5,1,0,-3]
    print("Tablica:", tabl)
    szukaj(tabl,0,len(tabl)-1, 7)
    szukaj(tabl,0,len(tabl)-1, 5)
    print("************** SILNIA ***************")
    for i in range(5,11):
        print (f"silnia({i}) = {silnia(i)}")
    print("************** Ciąg Fibonacciego ********")
    for i in range(1,12):
        print (f"fib({i})={fib(i)}")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
    
    
