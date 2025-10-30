# Odczytywanie daty i czasu systemowego
import datetime
import sys

def main(args):
    print ("Odczyt daty i czasu w formacie napisu")
    s = str(datetime.datetime.now())
    print (f" Czas i data bieżące - format pełny        {s}")
    print (f" Czas i data bieżące - format skrócony     {s[0:16]}")
    print ("Odczyt daty - dekompozycja składowych")
    dzis = str(datetime.date.today())
    print (" Wydruk w formie tekstowej:", dzis)
    dzis_rozszerz = datetime.datetime.strptime(dzis, "%Y-%m-%d")
    print (f" Dzień: {dzis_rozszerz.day}, miesiąc: {dzis_rozszerz.month}, rok: {dzis_rozszerz.year} ")

    print ("Odczyt daty i czasu - dekompozycja składowych")
    teraz = datetime.datetime.now()
    print(f" Data --> Dzień: {teraz.day}, miesiąc: {teraz.month}, rok: {teraz.year}")
    print (f" Czas --> Godzina: {teraz.hour}, minuta {teraz.minute}, sekunda: {teraz.second}")


if __name__=="__main__":
    sys.exit(main(sys.argv))

