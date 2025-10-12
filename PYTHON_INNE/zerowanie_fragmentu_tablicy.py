def zeruj(tab):
    i=0
    while i<len(tab):
        j=0
        while j<=i:
            tab[i][j]=0
            j=j+1
        i=i+1

def pisz(tab):
    for i in range (len(tab)):
        print(*tab[i])
        print()

def wypelnij(wymiar):
    lista = [[1 for _ in range(wymiar)] for _ in range(wymiar)]
    return lista

def main(args):
    tablica = wypelnij(6)
    pisz(tablica)
    print("#############################################")
    zeruj(tablica)
    pisz(tablica)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
    
    
    
