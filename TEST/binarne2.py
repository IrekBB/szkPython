import pickle
import sys

def main(args):
    with open ("binarne1.bin", "rb") as plik_in:
        pracownicy_z_dysku = None
        pracownicy_z_dysku=pickle.load(plik_in)
        print ("Słownik odczytany z dysku:")
        print (pracownicy_z_dysku)
    
    print ("Dodajemy nowy wpis do słownika odczytanego z dysku:")
    osoba = input("Podaj dane nowej osoby (Imię Nazwisko): ")
    telefon = input ("Podaj numer telefonu: ")
    pracownicy_z_dysku[osoba] = telefon
    print ("Słownik odczytany z pamięci komputera:")
    print (pracownicy_z_dysku)
    print ("Zapis zmodyfikowanego słownika na dysk")
    plik_out = open("binarne1.bin","wb")
    pickle.dump(pracownicy_z_dysku, plik_out)
    plik_out.close()
    print ("Uruchom program ponownie, aby sprawdzić wyniki!")


if  __name__=="__main__":
    sys.exit(main(sys.argv))