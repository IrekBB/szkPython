def szukaj(tab, x):
    n = len(tab)
    pos = 0
    while pos<n and tab[pos]!=x:
        pos+=1
    if pos<n:
        return pos
    else:
        return -1
            
def main(args):
    tabl=[1,2,3,2,-7,44,5,1,0,-3]
    while True:
        try:
            x = int(input("x="))
            break
        except ValueError:
            print("Oops!  Niepoprawna liczba.  Spróbuj jeszcze raz...")
    print (f"Szukamy {x}, {szukaj(tabl, x)}")
        
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
