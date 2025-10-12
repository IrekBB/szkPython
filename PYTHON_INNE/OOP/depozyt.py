class Depozyt:
    Limit = 50000 # Zmienna klasowa (limit sumy depozytów)
                  # Zmienna klasowa jest dostępna nawet, gdy nie utworzymy obiektów
    Suma = 0      # Zmienna klasowa (suma złozonych depozytów)

    def __init__(self, pWlasciciel, pDepozyt):
        self.__wlasciciel = pWlasciciel
        if pDepozyt + Depozyt.Suma <= Depozyt.Limit:
            # Dodajemy kolejny depozyt kliencki
            self.__zdeponowano = pDepozyt
            Depozyt.Suma = Depozyt.Suma + pDepozyt
        else:
            raise Exception("Odmowa! Depozyty przekroczyły limit promocyjny " + str(Depozyt.Limit) + "PLN")

    def __str__(self):  # Zwracany obiekt sformatowany do postaci napisu
        return "[ Właściciel:" + self.__wlasciciel + ", Kwota depozytu:" + str(self.__zdeponowano) + "]"

    def komunikat(self):
        print ("Cześć, jestem obiektem klasy Depozyt!")
    
    @property  # właściwość przeznaczona tylko do odczytu
    def wlasciciel(self):
        return self.__wlasciciel
    
    @property  # właściwość przeznaczona tylko do odczytu
    def depozyt(self):
        return self.__zdeponowano
    
    @depozyt.setter   # modyfikacja wartości atrybutu <nazwa>: @<nazwa>.setter
    def depozyt(self, korekta):
        staraWartosc = self.__zdeponowano
        if korekta + Depozyt.Suma - staraWartosc <= Depozyt.Limit:
            self.__zdeponowano = korekta
        else:
            raise Exception("Odmowa! Depozyty przekroczyły limit promocyjny " + str(Depozyt.Limit) + "PLN")
        # Dodajemy kolejny depozyt kliencki
        Depozyt.Suma = Depozyt.Suma - staraWartosc + korekta

def main(args):
    d1= Depozyt("Kowalski", 30000)
    print("Depozyt 'd1' to ", d1 )
    print("Suma depozytów to: ", Depozyt.Suma)

    d2= Depozyt("Nowak", 10000)
    print("Depozyt 'd2' to ", d2 )
    print("Suma depozytów to: ", Depozyt.Suma)

    d3= Depozyt("Wróbel", 10000)
    print("Depozyt 'd3' to ", d3 )
    print("Suma depozytów to: ", Depozyt.Suma)

    #d1.wlasciciel="Kowalska" #AttributeError: can't set attribute 'właściciel' (*)
    
    print ("Depozyt 'd3' utworzył ", d3.wlasciciel) 
    #print ("Depozyt 'd3' utworzył ", d3.__wlasciciel) #(**)

    print("Modyfikujemy depozyt d3 - wartość zmieniona na 5000")
    while True:
        try:
            d3.depozyt =  5000
            
        except:
            print ("Ups, przekroczono limitdepozytów.... Próbuj dalej.")    
            break
    
    print("Suma depozytów to: ", Depozyt.Suma)
    print("Depozyt 'd3' to teraz ", d3 )

    #Exception: Odmowa! Depozyty przekroczyły limit promocyjny 50000 PLN (***)
    while True:
        try:
            d3.depozyt=40000
            break
        except:
            print ("Ups, przekroczono limit depozytów.... Próbuj dalej.")

    d3.komunikat()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))