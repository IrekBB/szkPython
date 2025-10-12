from MojeTypy import BazaDanych as b
# ---------------------------------------------------------------------------------
# Przykłady użycia bazy danych osobowych
bazad=b.BazaDanych()
bazad.wstawSort("Kowalski", 2850)
bazad.wstawSort("Zarębski", 3100)
bazad.wstawSort("Fuks",     6700)
bazad.wstawSort("Nowak",    4000)
bazad.wstawSort("Konopek",  3350)
print ("Przed usunięciem nazwiska 'Nowak':")
bazad.wypiszNieposortowane("Baza nieposortowana")
print ("_________________________________________")
bazad.dane.usunWybrany("Nowak")
bazad.usunZIndeksuNazwisko("Nowak")
bazad.usunZIndeksuZarobek("Nowak")
bazad.wypiszNieposortowane("Baza nieposortowana po usunięciu nazwiska 'Nowak':")
bazad.wypiszSortZarobk("Baza posortowana według zarobków po usunięciu z indeksu zarobków nazwiska 'Nowak':")
bazad.wypiszSortNazw("Baza posortowana według nazwiski po usunięciu z indeksu nazwisk nazwiska 'Nowak':")
