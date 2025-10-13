import datetime
import math

class Pomiar(object):
    LimitNapiecia = 250  # Zmienna klasowa (limit pomiarowy)
    Licznik = 0  # Zmienna klasowa (liczba utworzonych obiektów)

    def __init__(self, pAutor, pOdczyt):
        self._dataczas = str(datetime.datetime.now())[0:19]  # [0:19] ogranicza ilość wyświetlanych znaków do: 2025-09-30 14:00:00
        # pojedyncze podkreślenie (_dataczas) oznacza teorerycznie pole tylko do odczytu
        self._autor = pAutor
        if math.fabs(pOdczyt) <= Pomiar.LimitNapiecia:
            self._odczyt = pOdczyt
        else:
            raise Exception("Odczyt nie może przekroczyć wartości " + str(Pomiar.LimitNapiecia))
        
        Pomiar.Licznik += 1 
    
    def __str__(self):
        return "Odczyt=" + str(self._odczyt) + " Dane kontrolne: |" + self._autor + "|" + self._dataczas
    
    @property   # Właściwośc przeznaczona tylko do odczytu
    def dataczas(self):
        return self._dataczas
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def odczyt(self):
        return self._odczyt
    
    @odczyt.setter
    def odczyt(self, korekta):
        if math.fabs(korekta) <= Pomiar.LimitNapiecia:
            self._odczyt = korekta
        else:
            raise Exception("Odczyt nie może przekroczyć wartości " + str(Pomiar.LimitNapiecia + "V"))
    def komunika(self):
        print ("Uwaga: obiekt klasy [Pomiar]")


class PomiarV(Pomiar):
    DolnyLimit = 100
    GornyLimit = 200

    def __init__(self, pAutor, pOdczyt, pNrSeryjny):
        super().__init__(pAutor, pOdczyt)
        if pOdczyt >= PomiarV.DolnyLimit  and pOdczyt <= PomiarV.GornyLimit:
            self_odczyt = pOdczyt
        else:
            raise Exception("Błąd zakresu")
        self._nrseryjny = pNrSeryjny
    

    def odczyt(self, korekta):
        if korekta >= PomiarV.DolnyLimit and korekta <= PomiarV.GornyLimit:
            self_odczyt = korekta
        else:
            raise Exception("Błąd zakresu")
    
    def __str__(self):
        s = super().__str__()
        return s + " Nr seryjny="+self._nrseryjny
    
    def komunikat(self):
        print ("Uwaga: obiekt klasy [PomiarV]") 




if __name__ == "__main__":
    print ("Jest moduł. Testuj go za pomoca skrypletu MainPomiar.py")
    
    
