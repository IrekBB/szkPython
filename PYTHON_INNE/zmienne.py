def zmienne():
    mojKod = 0
    mojParametr = 3.14
    print("#1. mojParametr=", mojParametr)
    wielkaLiczba=4.34561e13
    mojNapis="Cześć"
    
    mojaLista={"ala", "ma", "kota"}   #kolekcja typu set
    print( "mojKod:",        mojKod,      " --> ", type(mojKod), "\n",
           "mojParametr:",   mojParametr, " --> ", type(mojParametr), "\n",
           "mojNapis:",      mojNapis,    " --> ", type(mojNapis), "\n",
           "mojaLista",      mojaLista,   " --> ", type(mojaLista), "\n",)

    print("Wielka liczba=", wielkaLiczba)
    print ("Ponowne wykorzystanie identyfikatora zmiennej:")
    mojParametr = "X-12"
    print( "mojParametr:",   mojParametr,      " --> ", type(mojParametr), "\n")
    z1 = 2 + 3j
    z2 = 3 - 4j
    print ("Typ zmiennej z1 to: ", type(z1))
    print(z1+z2)

def main(args):
    zmienne()

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
    
           
