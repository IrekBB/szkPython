from MojeModuly import ListaTab as t

def main(args):
    T = t.ListaTab(4)
    T.WstawNaKoniec("1-Kowalski", 30)
    T.WstawNaKoniec("2-Kowalska", 28)
    T.WstawNaKoniec("3-Nowak", 35)
    T.WstawNaKoniec("4-Pankracy", 45)
    T.WstawNaKoniec("5-Nadmiarowy", 5)
    T.wypisz("Lista finalna: ")
    T.wypisz("Próba wstawienia rekordu 'Newton' na trzecia pozycję")
    T.WstawNaPozycje("*Newton*", 378, 2)
    T.usunOsobe("Nie ma mnie")
    T.usunOsobe("3-Nowak")
    T.wypisz("Po usunięciu rekrdu '3-Nowak'")
    T.wypisz("Próba wstawienia rekordu '*Newton* na drugą pozycję")
    T.WstawNaPozycje("*Newton*", 378, 2)
    T.wypisz("Lista finalna")



if __name__== "__main__":
    import sys
    sys.exit(main(sys.argv))