"""
subprocess.Popen() to interfejs niższego poziomu służący do uruchamiania podprocesów.
Subprocess.run jest jego wrapperem (interfejsem wyższego poziomu).

Popen() umożliwia rozpoczęcie nowego procesu i zarządzanie standardowymi strumieniami wejściowymi, wyjściowymi i błędu.
Zwraca uchwyt do działającego procesu, którego można użyć do oczekiwania na zakończenie procesu, sprawdzenia jego kodu 
powrotu lub jego zakończenia.

run() w przeciwieństwie do subrocess.Popen() jest wygodniejszą funkcją, która umożliwia uruchomienie polecenia i przechwycenie 
jego wyników w jednym wywołaniu, bez konieczności tworzenia obiektu Popen i samodzielnego zarządzania strumieniami. 
Umożliwia także określenie różnych opcji uruchamiania polecenia, na przykład tego, czy zgłosić wyjątek w przypadku
niepowodzenia wykonania polecenia.

Kiedy uzywać funkcji run?
Ogólnie rzecz biorąc, powinieneś używać funkcji run(), jeśli chcesz tylko uruchomić polecenie i przechwycić jego dane wyjściowe.
Kiedy Popen?
Popen, jeśli potrzebujesz większej kontroli nad procesem, na przykład interakcji ze strumieniami wejściowymi i wyjściowymi. 
Klasa Popen przyjmuje te same argumenty co run(), łącznie z argumentami określającymi polecenie, które ma zostać uruchomione,
oraz innymi opcjonalnymi argumentami, takimi jak stdin, stdout, stderr, Shell, cwd i env. Ponadto klasa Popen ma kilka metod 
umożliwiających interakcję z procesem, takich jak communicate(), poll(), wait(), termin() i kill().
"""

def main(args):
    p = subprocess.Popen(["python", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = p.communicate()
    print(output)
"""
Powyższe polecenie, spowoduje uruchomienie polecenia python –help i utworzenie nowego obiektu Popen, 
który będzie przechowywany w zmiennej p. Standardowe wyjście i wyjście strumienia błędu są przechwytywane 
za pomocą metody communicate() i zapisywane odpowiednio w zmiennych wyjściowych i zmiennych strumiena błędu.
subprocess.Popen jest przydatny, gdy chcesz mieć większą kontrolę nad procesem, np. wysyłać do niego dane 
wejściowe, odbierać z niego dane wyjściowe lub oczekiwać na jego zakończenie. 

"""
if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))