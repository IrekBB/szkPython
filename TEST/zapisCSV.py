import csv       # comma separated values
import pathlib
import sys

def main(args):
    nazwapliku = "seria-output.csv"
    pomiary = [ [15.2,2.1,3.2,3.3,5.5,6.60,1.01],
               [5.2, 1.30, 2.330, 8.30, -4.50, -6.23,1.01],
               [3.22, 20,50,50, 70,80,1.20],]
    plik = (pathlib.Path(r"E:\Users\opiekun\Documents\szkPython\TEST") / pathlib.Path(nazwapliku)).open(mode="w", newline='\r\n')
    CSVwriter=csv.writer(plik)
    print ("Zapisujemy wiersze do pliku CSV na podstawie listy:")
    print(pomiary)
    for wiersz in pomiary:
        CSVwriter.writerow(wiersz)
    plik.close()
    
    print ("Sprawdzam zawartość pliku  CSV:")
    plik = (pathlib.Path(r"E:\Users\opiekun\Documents\szkPython\TEST") / pathlib.Path(nazwapliku)).open(mode="r", newline='')
    print (plik.read())
    plik.close()


if __name__ =="__main__":
    sys.exit(main(sys.argv))