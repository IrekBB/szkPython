def main(args):
    tab = [s.Element("Jan", 20), s.Element("Marek", 10), s.Element("Maria",15), s.Element("Zośka", 13)]
    print ("Szukam imie='Maria' ", s.szukajGen(tab, "Maria", s.porownaj_imiona) != len(tab))
    print ("Szukam imie='Marja' ", s.szukajGen(tab, "Marja", s.porownaj_imiona) != len(tab))
    print ("Szukam wiek=132 ", s.szukajGen(tab, 132, s.porownaj_wiek) != len(tab))
    print ("Szukam wiek=13 ", s.szukajGen(tab, 13, s.porownaj_wiek) != len(tab))

if __name__ == "__main__":
    from MojeTypy import szukaj as s
    import sys
    sys.exit(main(sys.argv)) 