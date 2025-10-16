"""
# Usuwanie pliku w Pythonie przy użyciu modułu os
import os

# Ścieżka do pliku, który chcemy usunąć
sciezka_do_pliku = 'e:\Folder_2\plik.txt'

# Sprawdzenie, czy plik istnieje
if os.path.exists(sciezka_do_pliku):
    # Usunięcie pliku
    os.remove(sciezka_do_pliku)
    print(f"Plik {sciezka_do_pliku} został usunięty.")
else:
    print(f"Plik {sciezka_do_pliku} nie istnieje.")

#FileNotFoundError, Usuwanie plików
import os

sciezka_do_pliku = 'plik_do_usuniecia.txt'

try:
    os.remove(sciezka_do_pliku)
    print(f"Plik {sciezka_do_pliku} został usunięty.")
except FileNotFoundError as e:
    print(f"Błąd podczas usuwania pliku {sciezka_do_pliku}: {e}")

# Kopiowanie pliku w Pythonie przy użyciu modułu shutil
# Do kopiowania plików możemy użyć modułu shutil, a konkretnie funkcję copyfiles():    

import shutil

# Ścieżka pliku źródłowego i docelowego
plik_zrodlowy = 'e:\Folder_1\plik.txt'
plik_docelowy = 'e:\Folder_2\plik.txt'

# Skopiowanie pliku z plik_zrodlowy.txt do plik_docelowy.txt
shutil.copyfile(plik_zrodlowy, plik_docelowy)

print("Plik został skopiowany.")

# Zapis polskich znaków do pliku tekstowego

plik2 = open('plik2.txt', 'w', encoding='utf-8')

# zapisz treść do plik2.txt
plik2.write('Zapisana treść do pliku.\n')
plik2.write('Koniec pliku.\n')
plik2.close()

# Peklowanie
import pickle

# Tworzenie przykładowego słownika
dane = {
    'imię': 'Jan',
    'wiek': 30,
    'miasto': 'Warszawa'
}

# Zapisywanie słownika do pliku za pomocą pickle
with open('dane.pickle', 'wb') as plik:
    pickle.dump(dane, plik)

# Odczytywanie słownika z pliku za pomocą pickle
with open('dane.pickle', 'rb') as plik:
    wczytane_dane = pickle.load(plik)

print("Wczytane dane:", wczytane_dane)

# Pliki csv
import csv

# Otwórz plik CSV w trybie odczytu
with open('kontakty.csv', 'r') as csvfile:

    # Utwórz obiekt reader
    reader = csv.reader(csvfile, delimiter=',')

    # Pomiń nagłówek
    next(reader, None)

    # Iteruj po wierszach pliku
    for row in reader:
        print(row)

# Otwórz plik CSV w trybie dopisywania
with open('kontakty.csv', 'a', newline='', encoding='utf-8') as csvfile:

    # Utwórz obiekt writer
    writer = csv.writer(csvfile, delimiter=',')

    # Zapisz wiersze do pliku
    writer.writerow(['Rafał', 'Marcinkiewicz', 'rafal.marcinkiewicz@email.pl', '34545634'])        

"""