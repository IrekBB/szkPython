import sys
import datetime

def main(args):
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dzis = str(datetime.date.today())
    print(dzis)
    dzis_rozszerz = datetime.datetime.strptime(dzis, "%Y-%m-%d")
    print(dzis_rozszerz)
    dzien = int(dzis_rozszerz.day)
    miesiac = int (dzis_rozszerz.month)
    rok = int (dzis_rozszerz.year)
    
    if (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400  == 0):    # Czy rok jest przestępny
        dni[1] = 29
    
    print(f"Dzień: {dzien}, miesiąc: {miesiac}, rok: {rok}")
    print("Liczba dni w miesiącu wynosi:", dni[miesiac-1])



if __name__=="__main__":
    sys.exit(main(sys.argv))