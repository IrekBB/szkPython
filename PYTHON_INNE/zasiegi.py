def zasieg():
    wynik = 6
    print ("wynik=", wynik)
    def pi_razy_drzwi(pi, dzrzwi):
        x=5
        wynik= pi*dzrzwi
        print ("wynik=", wynik)
    pi_razy_drzwi(3,4)

def funkcyjka ():
    global v
    v=5
    print ("Wywołanie wv funkcji funkcyjka(), v=", v)



    

if __name__=="__main__":
    v=int() # pusta deklaracja zmiennej globalnej typu int
    funkcyjka()
    zasieg()
    v=v+1
    print("Wywołanie v w skrypcie głównym, v=", v)


