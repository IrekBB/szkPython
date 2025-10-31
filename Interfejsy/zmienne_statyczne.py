"""
Statyczne zmienne klasowe w Pythonie to zmienne współdzielone przez wszystkie instancje klasy, 
definiowane bezpośrednio w przestrzeni klasowej, poza jakimikolwiek metodami. 
Służą do przechowywania danych, które są wspólne dla wszystkich obiektów danej klasy, 
w przeciwieństwie do zmiennych instancji, które są unikalne dla każdego obiektu. 

*** Współdzielenie danych: 
Pozwalają na współdzielenie danych między wszystkimi instancjami klasy.

*** Definicja: 
Są definiowane na poziomie klasy, a nie wewnątrz metod __init__ lub innych metod instancji.

*** Dostęp: Dostęp do nich można uzyskać zarówno poprzez samą klasę (np. Klasa.zmienna), 
jak i poprzez instancję (np. obiekt.zmienna), choć dostęp przez klasę jest bardziej typowy i jednoznaczny. 
"""
class Licznik:
    liczba_obiektow = 0  # Zmienna statyczna (klasowa)

    def __init__(self):
        Licznik.liczba_obiektow += 1

def main(args):
    # Tworzenie instancji
    obj1 = Licznik()
    obj2 = Licznik()
    obj3 = Licznik()

    # Odczytanie wartości zmiennej statycznej
    print(Licznik.liczba_obiektow)  # Wypisze: 3
    print(obj1.liczba_obiektow)     # Wypisze: 3

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))