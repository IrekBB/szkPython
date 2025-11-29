"""
Docstring for python subprocess run
subprocess.run() pozwala uruchomić podproces, oczekając na jego zakonczenie.
Po uruhomieniu podprocesu metoda run() blokuje się do czasu zakończenia podprocesu i 
zwrócenia przez niego obiektu CompletedProcess, ktory zawiera zwracany kod
i wyjście podprocesu.
Argumenty:
* args: Wywoływana komenda z argumentami przekazywanymi jako lista stringów
* capture_output: jeśli True, przechwytuje standardowe wyjście i standardowe wyjście błędów
* text: jeśli True, zwraca standardowe wyjście i błąd jako stringi, w drugim przypadku jako ciag bajtów
* check: określa, czy kontrolować kod zwracany przez podproces, jeśli jest ustawiony na True i zwaracany
  kod istnieje rzuca wyjątkiem  CalledProcessError
* timeout: wartość w sekundach określająca czas oczekiwania na zakończenie podprocesu przed upływem limitu czasu
* shell: Wartość logiczna wskazująca, czy uruchomić polecenie w powłoce. Oznacza to, że polecenie jest
  przekazywane jako ciąg znaków i można używać funkcji specyficznych dla powłoki, takich jak rozwijanie
  symboli wieloznacznych i podstawianie zmiennych. 

  Obiekt CompletedProcess i jego atrybuty:
  * args: polecenia i argumnety z którymi proces został uruchomiony
  * returncode: kod zwracany (powrotu) podprocesu
  * stdout: standardowe wyjscie podprocesu(string jesli test=True, w innym przypadku bajty)
  * stderr: standardowe wyjście błędu procesu (string jeśli text=True, w innym przypadku bajty )

"""


def main(args):
    result = subprocess.run("dir", shell=True, capture_output=True, text=True)
    print(result.stdout)

if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))

"""
Na linuksie:
result = subprocess.run(["ls", "-la"], capture_output=True, text=True) (no shell argument needed)
"""