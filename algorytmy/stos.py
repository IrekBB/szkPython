class StosOgraniczony:
    def __init__(self, pRozmiar):
        self._stos = list()      # Włacśiwa kolekcja danych
        self._MaxElt = pRozmiar # Maksymalny rozmiar stosu

    def zeruj(self):  # zerowanie stosu
        self._stos.clear()

    def wypisz(self, s):
        print(s)
        if self._stos!=None:
            print (" Zawartość stosu: [", end=" ")
            for x in self._stos:
                print(x, end=" ")
            print("]")

    def push(self, obj):
        print("Odkładam: ",str(obj))   # Konwersja na postać tekstową
        if len(self._stos) < self._MaxElt:
            self._stos.append(obj)  # Dokładamy kolejny element na koniec
        else:
            print("* POJEMNOŚĆ PRZEKROCZONA *")

    def pop(self):
        if len(self._stos)>0:
            tmp = self._stos.pop() # Pobieramy ostatni element
        return tmp # Usuwamy ze stosu, ale nie tracimy dostępu do elementu usuwanego

def pobierz():
    tekst = input('Wyrażenie ONP: ')
    return tekst.split()


def main(args):
    stos = StosOgraniczony(100)
    for obj in pobierz():
        if obj not in ('+','-','*','/','//'):
            stos.push(obj)
        else:
            a = stos.pop()
            b=  stos.pop()
            c = eval(b + obj + a)
            stos.push(str(c))
    stos.wypisz('Na stosie')
    
            

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
