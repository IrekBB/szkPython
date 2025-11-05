# Formularze wprowadzania danych (multenterbox)
import easygui
import sys

def main(args):
    msg = "Podaj parametry testu"
    title = "Warunki brzegowe"
    pola = ["Min", "Max", "Krotność","Odchyłka"]
    wyniki = easygui.multenterbox(msg, title,pola)

    while 1:  # Wymuszone wprowadzenie każdej wartości
        if wyniki is None: # Nie dokonano wyboru
            break
        errmsg = ""   # Tworzymy komunikat błędu
        for i in range(len(pola)):
            if wyniki[i].strip() =="":
                errmsg += ('"Pole %s" jest wymagane.\n' % pola[i])
        if errmsg=="":
            break
        wyniki = easygui.multenterbox(errmsg, title,pola, wyniki)
    print("Wprowadzono: ", str(wyniki))  
    # Pojedyncze pole
    msg = "Podaj wartość"
    title = "Liczba przebiegów"
    wynik = easygui.enterbox(msg, title)
    print ("Podano ", wynik)



if __name__=="__main__":
    sys.exit(main(sys.argv))
