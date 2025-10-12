def szukaj(tab,x):
    left=0
    right=len(tab)-1
    mid = 0
    znaleziono = False
    while (left<=right) and (not znaleziono):
        mid = (left+right)//2
        if tab[mid]==x:
            znaleziono=True
        else:
            if tab[mid]<x:
                left=mid+1
            else:
                right=right-1
    if znaleziono == True:
        return mid
    else: return -1

def main(args):
    tab = [1,2,6, 18, 20, 23, 29, 32,34, 39, 40, 41]
    for i in range (0, len(tab)):
        print(f"t[{i}]={tab[i]}", end=" ")
    print (f"Szukam 23, wynik: {szukaj(tab, 23)}")
    print (f"Szukam 3, wynik: {szukaj(tab, 3)}")
    
        
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
