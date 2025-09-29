"""
Instrukcja obsługi skryptu RSA

Generacja kluczy
W pierwszej części formularza wygeneruj parę kluczy: publiczny i prywatny.
Zachowaj je i wyczyść klucze, aby nikt nie mógł ich odczytać.

Szyfrowanie/Rozszyfrowywanie
W drugiej części formularza wprowadź odpowiedni klucz (wykładnik oraz moduł),
wiadomość i kliknij przycisk "koduj RSA". Wynik zostanie wyświetlony poniżej.
Uwaga:
Na podstawie podanych informacji napiszemy prostą aplikację,
która pełnić będzie rolę kompletnego systemu szyfrowania RSA.
Proces szyfrowania i rozszyfrowywania jest identyczny, różni
się tylko rodzajem zastosowanego klucza. Dlatego w aplikacji
występują jedynie dwie opcje: tworzenie kluczy RSA oraz
szyfrowanie RSA. W pierwszym przypadku program generuje dwa
klucze, publiczny oraz prywatny. Należy zapamiętać te dane,
gdyż będą one potrzebne w drugiej opcji do szyfrowania lub
rozszyfrowywania. Proponujemy zastosowanie tej aplikacji do
prostej zabawy w klasie. Tworzymy jedną grupę uczniów, która
utworzy klucz publiczny oraz prywatny. Klucz publiczny przekaże
reszcie klasy, klucz prywatny zachowa dla siebie. Następnie
pozostali uczniowie na podstawie otrzymanych kluczy publicznych
mogą kodować swoje dane i przekazywać je pierwszej grupie, która
za pomocą klucza prywatnego dokona rozszyfrowania wiadomości.

"""
#Python (dodatek)
# *******************************************************
# ** Przykładowa aplikacja obrazująca sposób działania **
# ** asymetrycznego systemu kodowania informacji RSA.  **
# ** ------------------------------------------------- **
# **           (C)2024 mgr Jerzy Wałaszek              **
# **            I Liceum Ogólnokształcące              **
# **          im. Kazimierza Brodzińskiego             **
# **                   w Tarnowie                      **
# *******************************************************

import random
from os import system, name


# Funkcja czeka na dowolny klawisz i czyści ekran
# ------------------------------------------------
def czekaj():
    print()
    input("Zapisz te dane i naciśnij Enter")
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


# Funkcja obliczająca NWD dla dwóch liczb
# ----------------------------------------
def nwd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


# Funkcja obliczania odwrotności modulo n
# ----------------------------------------
def odwr_mod(a, n):
    p0 = 0
    p1 = 1
    a0 = a
    n0 = n
    q = n0 // a0
    r = n0 % a0
    while r > 0:
        t = p0 - q * p1
        if t >= 0:
            t %= n
        else:
            t = n - ((-t) % n)
            p0 = p1
            p1 = t
            n0 = a0
            a0 = r
            q = n0 // a0
            r = n0 % a0
    return p1


# Procedura generowania kluczy RSA
# ---------------------------------
def klucze_rsa():
    tp = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    print("Generowanie kluczy RSA")
    print("----------------------")
    print()
    # generujemy dwie różne, losowe liczby pierwsze
    while True:
        p = tp[random.randrange(10)]
        q = tp[random.randrange(10)]
        if p != q: break
    phi = (p - 1) * (q - 1)
    n = p * q
    # wyznaczamy wykładniki e i d
    e = 3
    while nwd(e, phi) != 1:
        e += 2
    d = odwr_mod(e, phi)
    # gotowe, wypisujemy klucze
    print("KLUCZ PUBLICZNY")
    print("wykładnik e =", e)
    print("    moduł n =", n)
    print()
    print("KLUCZ PRYWATNY")
    print("wykładnik d =", d)
    czekaj()


# Funkcja oblicza modulo potęgę podanej liczby
# ---------------------------------------------
def pot_mod(a, w, n):
    # wykładnik w rozbieramy na sumę potęg 2
    # przy pomocy algorytmu Hornera. Dla reszt
    # niezerowych tworzymy iloczyn potęg a modulo n.
    pot, wyn, q = a, 1, w
    while q > 0:
        if q % 2 != 0:
            wyn = (wyn * pot) % n
        pot = (pot * pot) % n  # kolejna potęga
        q //= 2
    return wyn


# Procedura kodowania danych RSA
# -------------------------------
def kodowanie_rsa():
    print("Kodowanie danych RSA")
    print("--------------------")
    print()
    e = int(input("Podaj wykładnik = "))
    n = int(input("    Podaj moduł = "))
    print("----------------------------------")
    print()
    t = int(input("Podaj kod RSA   = "))
    print()
    print("\nWynik kodowania =", pot_mod(t, e, n))
    czekaj()


# ********************
# ** Program główny **
# ********************

while True:
    print("System szyfrowania danych RSA")
    print("-----------------------------")
    print(" (C)2024 mgr Jerzy Wałaszek")
    print()
    print("MENU")
    print("====")
    print("[0]-Koniec pracy programu")
    print("[1]-Generowanie kluczy RSA")
    print("[2]-Kodowanie RSA")
    print()
    w = int(input("Jaki jest twój wybór? (0, 1 lub 2) : "))
    print()
    print()
    print()
    match w:
        case 0:
            break
        case 1:
            klucze_rsa()
        case 2:
            kodowanie_rsa()
    print()
    print()
    print() 
