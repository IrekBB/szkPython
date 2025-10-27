import sys
import csv
import pathlib

pomiary = [
    {"Miernik": "Sonel", "Data": "2021-05-20", "Odczyt": 130.42},
    {"Miernik": "CEM", "Data": "2021-05-20", "Odczyt": 129.13},
    {"Miernik": "Fluke", "Data": "2021-05-21", "Odczyt": 130},
    {"Miernik": "Fluke", "Data": "2021-05-21", "Odczyt": 119.99},
    {"Miernik": "Voltcraft", "Data": "2021-05-21", "Odczyt": 131.01},
]

def main(args):
    plik = pathlib.Path (r"E:\Users\opiekun\Documents\szkPython\TEST\serieH-output.csv").open(mode="w", encoding="utf-8", newline='')
    CSVwriter=csv.DictWriter(plik, fieldnames=["Miernik", "Data", "Odczyt"])
    CSVwriter.writeheader()  # Zapis wiersza nagłówka
    CSVwriter.writerows(pomiary)  # Zapis pozostałych wierszy
    plik.close()
    print (f"Sprawdzamy zawartość pliku '{plik.name}':")
    plik = pathlib.Path (r"E:\Users\opiekun\Documents\szkPython\TEST\serieH-output.csv").open(mode="r", encoding="utf-8", newline='')
    print (plik.read())
    plik.close()



if __name__=="__main__":
    sys.exit(main(sys.argv))