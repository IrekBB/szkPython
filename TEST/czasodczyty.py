import time

"""
Inne poiżyteczne funkcje:
sleep(n)  - wstrzymuje działanie programu na n sekund
Przeliczanie czasów generowanych w róznych strefach czasowych
time.tzname - tutaj możesz odczytać nazwę strefy czasowej, np. 'CET', 'CEST'
time.timezone - zwraca przesunięcie bieżącej strefy lokalnej względem czasu UTC (w Polsce -3600, jedna godzina)

"""

def main(args):
    sekundnik = time.time()
    GMT = time.gmtime()  # Czas UTC/GMT
    Lok = time.localtime()   # Czas lokalny

    print (f"Liczba sekund od dziejów zarania to {sekundnik}")
    print ("Czas bieżący tzw. uniwersalny (UTC albo GMT):\n", GMT) 
    print (f" Rok {GMT.tm_year}, miesiąc {GMT.tm_mon}, dzień {GMT.tm_mday}")
    print (f" Godzina {GMT.tm_hour}, miesiąc {GMT.tm_min}, dzień {GMT.tm_sec}")
    print (f" Dzień tygodnia(0-6) {GMT.tm_wday}, dzień roku (1-366): {GMT.tm_yday}, znacznik DST: {GMT.tm_isdst}")  # DST - znacznik czasu letniego
    print (f" Czas bieżący tzw. uniwersalny (UTC albo GMT):\n{GMT}:")
    print ("Czas lokalny:")
    print (f" Godzina {Lok.tm_hour}, minuta {Lok.tm_min}, sekunda {Lok.tm_sec}")
    print (f" Znacznik czasu letniego: {Lok.tm_isdst}")
    print ("Funkcja 'ascitime':", time.asctime())

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
