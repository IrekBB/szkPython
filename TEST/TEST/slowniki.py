pracownicy = {
    "Jan Kowalski"    :     668168555,
    "Anna Zwinna"     :     605123001,
    "Marek Ekspercki" :     721003050,
    "Jan Bęcki"       :     672000455,
}

def main(args):
    for imie, numer in pracownicy.items():
        print (f"Pracownik: {imie}, telefon:\t{numer}")
    print(pracownicy)
    nazwisko = input("Podaj nazwisko osoby: ")
    if nazwisko in pracownicy:
        print (f"Znalazłem {nazwisko} w bazie danych!")
    else:
         print (f"Nie znalazłem {nazwisko} w bazie danych!")
    # przypadek: klucz istnieje
    print ("klucz: Jan Bęcki, wartość: ", pracownicy.get("Jan Bęcki "))
    # przypadek: brak klucza
    print ("klucz: Janek Bęcki, wartość: ", pracownicy.get("Janek Bęcki "))   # zwraca None, jak to obsłużyć?
    print ("klucz: Janek Bęcki, wartość: ", pracownicy.get("Janek Bęcki ", "Nie znaleziono wpisu!"))
    # Dodawanie wpisów do słownika 
    print ("Rozszerzanie słownika  o nowe wpisy (Piotr Wróblewski, tel. 668999550): ")
    pracownicy["Piotr Wróblewski"]= 668999550
    print(pracownicy)
    print ("Aktualizacja zawartości słownika dla wczesniej uzytego klucza (Piotr Wróblewski, nowy tel. 668888550)")
    pracownicy["Piotr Wróblewski"]= 668888550
    print (pracownicy)
    # Usunięcie elementu ze słownika
    nazwisko = input("Podaj nazwisko osoby do usunięcia: ")
    if nazwisko in pracownicy:
        print (f"Znalazłem \'{nazwisko}\' w slowniku, usuwam!!!!")
        pracownicy.pop(nazwisko)
    else:
        print (f"Nie znalazłem \'{nazwisko}\' w slowniku")
    print ("Finalna zawartość listy pracowników")
    print(pracownicy)
    




if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))