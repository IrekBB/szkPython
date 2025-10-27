import sys
import csv
import pathlib

def main(args):
    plik = pathlib.Path (r"E:\Users\opiekun\Documents\szkPython\TEST\serieH.csv").open(mode="r", encoding="utf-8", newline='')
    CSVreader = csv.DictReader(plik, delimiter=",")
    print ("Etykiety kolumn wiersza nagłówkowego:", CSVreader.fieldnames)
    
    print ("Wartości w słowniku można adresować, używając etykiet z wiersza nagłówkowego:")
    print (f"{CSVreader.fieldnames[0]:11}  {CSVreader.fieldnames[1]:5} {CSVreader.fieldnames[2]:6}  {CSVreader.fieldnames[3]}")
    for w in CSVreader:
        print (f"{w['Imię']:10}  {w['Nazwisko']:11}  {w['Wiek']:5}  {float (w['Płaca']):8.2f} ")
    print ("zawartość odczytanego pliku CSV odczytana jako lista slówników Pythona")
    plik.seek(0)
    for w in CSVreader:
        print(w)
    plik.close()

if __name__=="__main__":
    sys.exit(main(sys.argv))