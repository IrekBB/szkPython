class Element:
    def __init__(self, pNazwisko="Doe", pWiek=0 ):
        self.nazwisko = pNazwisko
        self.wiek = pWiek
        self.nastepny = None
        self.poprzedni = None

# Proba bezpośredniego wywołania modułu
if __name__ == "__main__":
	print("To jest moduł biblioteczny, aby przetestować wywołaj plik:", "Lista2KierMain.py!")