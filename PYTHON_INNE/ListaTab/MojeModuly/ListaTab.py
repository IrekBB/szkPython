from MojeModuly import Fiszka as f

class ListaTab:
	def __init__(self, MaxTab):
		self.tab = [f.Fiszka() for _ in range(MaxTab)] # Tworzy statyczna tablicę o rozmiarze MaxTab
		self.Licznik = 0  # Poczatkowa liczba wpisów równa 0
		self.Rozmiar = MaxTab  # Maksymlny rozmiar tablicy
	def wypisz(self, s):
		print(s)
		for i in range(0, self.Licznik):
			print (f"[{self.tab[i].nazwisko}, {self.tab[i].wiek}]", end =" ")
		print()
	def szukaj (self, pNazwisko):
		for i in range (0, self.Licznik):
			if self.tab[i].nazwisko == pNazwisko:
				return i
		return -1
	def usunOsobe(self, pNazwisko):
		k = self.szukaj(pNazwisko)
		print (f"Indeks poszukiwanej pozycji '{pNazwisko}': {k}")
		if k>=0:
			for i in range(k, self.Licznik-1):
				self.tab[i] = self.tab[i+1]
			self.Licznik = self.Licznik - 1
	def WstawNaKoniec(self, pNazwisko, pWiek):
		if self.Licznik < self.Rozmiar:
			nowy = f.Fiszka(pNazwisko, pWiek)
			self.tab[self.Licznik] = nowy
			self.Licznik = self.Licznik + 1
		else:
			print (f"Tablica pełna, nie wstawiono: ({pNazwisko}, {pWiek})!")
			
	def WstawNaPozycje(self, pNazwisko, pWiek, k):
		if self.Licznik == self.Rozmiar or k not in range(0, self.Licznik):
			print(f"--- Tablica pełna/błędny indeks: nie wstawiono: ({pNazwisko}, {pWiek})")
			return
		nowy = f.Fiszka(pNazwisko, pWiek)
		for i in range(self.Licznik-1, k , -1):
			self.tab[i] = self.tab[i+1]
		self.tab[k] = nowy
		self.Licznik = self.Licznik + 1	
			
# Proba bezpośredniego wywołania modułu
if __name__ == "__main__":
	print("To jest moduł biblioteczny, aby przetestować wywołaj plik:", "ListaTabMain.py!")
