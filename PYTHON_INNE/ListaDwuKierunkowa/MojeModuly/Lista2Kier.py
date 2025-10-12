from MojeModuly import Element as E
class Lista2Kier:
    def __init__(self):
        self.glowa = None
        self.ogon = None
    def wstaw(self, pNazwisko, pWiek):  
        nowy = E.Element(pNazwisko, pWiek)
        if self.glowa != None:
            self.ogon.nastepny = nowy
            nowy.poprzedni = self.ogon
            self.ogon = nowy
        else:
            self.glowa = nowy
            self.ogon = nowy
    def szukaj (self, pNazw):
         tmp=self.glowa  # Zmienna zapamietująca status przeszukiwania listy
         znaleziono=False
         while tmp!=None:
              if tmp.nazwisko==pNazw:
                   znaleziono = True
                   break
              else:
                   tmp = tmp.nastepny
         if znaleziono == True:
              return tmp, True
         else:
              return None, False
    def usun(self, pNazw):
         res, znaleziono = self.szukaj(pNazw)
         if znaleziono == False:
              print(f"Brak [{pNazw}] na liście")
              return
         print(f"Usuwam [{pNazw}] z listy")

         if res.poprzedni != None and res.nastepny != None:     # Usuwam ze środka
              res.poprzedni.nastepny = res.nastepny
              res.nastepny.poprzedni = res.poprzedni.nastepny
              return

         if res == self.glowa:   # Usuwanie z przodu
              self.glowa = res.nastepny
              res.nastepny.poprzedni = None
         else:
              res.poprzedni.nastepny = None   # Usuwanie z tyłu 
              self.ogon = res.poprzedni
    def wypiszWprzod(self, s):
         print(s)
         tmp = self.glowa
         while tmp != None:
             print (f"[{tmp.nazwisko}, {tmp.wiek}]", end =" ") 
             tmp = tmp.nastepny
         print("")
    def wypiszWstecz(self, s):
         print(s)
         tmp = self.ogon
         while tmp != None:
             print (f"[{tmp.nazwisko}, {tmp.wiek}]", end =" ") 
             tmp = tmp.poprzedni
         print("")

    


# Proba bezpośredniego wywołania modułu
if __name__ == "__main__":
	print("To jest moduł biblioteczny, aby przetestować wywołaj plik:", "Lista2KierMain.py!")

