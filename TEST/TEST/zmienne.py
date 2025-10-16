def main(args):
    mojKod = 0
    mojParametr = 3.14
    wielkaLiczba = 4.34561e13
    mojNapis = "Napis"
    mojaLista = {'ala', 'ma','kota'}
    print (mojKod,"---", type(mojKod), "\n",
           mojParametr,"---", type(mojParametr),"\n",
           mojNapis,"---", type(mojNapis),"\n",
           mojaLista,"---", type(mojaLista),"\n",
           )
    print ("Wielka liczba=", wielkaLiczba)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
