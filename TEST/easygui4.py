import easygui
import sys

def main(args):
    # Miniedytor lub panel podglądu tekstu (codebox)
    res =easygui.codebox(msg="Nowa oferta", title="Ogłoszenie", text = "Aaaaby sprzedać\nAaaaale wcaaaaleeee\nniedrogo")
    print (res)

if __name__=="__main__":
    sys.exit(main(sys.argv))