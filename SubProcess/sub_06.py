"""
Funkcja subprocess.call()

subprocess.call() to funkcja modułu podprocesu Pythona, która służy do uruchamiania polecenia w 
oddzielnym procesie i oczekiwania na jego zakończenie. Zwraca kod powrotu polecenia, który wynosi zero, 
jeśli polecenie się powiodło  i warość różną od zera, jeśli się nie powiodło.

Funkcja call() ma te same argumenty co funkcja run (właczając w to argumenty określające polecenie, 
które ma zostać uruchomione)  oraz inne opcjonalne argumenty, takie jak stdin, stdout, stderr, Shell, cwd i env.
Standardowe wyjście i błąd polecenia są wysyłane na to samo standardowe wyjście i wyjscie błędu (stderr), 
co proces nadrzędny, chyba że przekierujesz je za pomocą argumentów stdout i stderr.

"""

def main(args):
    return_code = subprocess.run([sys.executable, "--version"]).returncode  
    if return_code == 0:  
        print("Command executed successfully.")  
    else:  
        print("Command failed with return code", return_code)
    
    c = subprocess.call("(dir /a/q)", shell=True)
    print("Return code:", c)
"""
Spowoduje to uruchomienie polecenia python --version w oddzielnym procesie i poczekanie na jego zakończenie. 
Kod powrotu polecenia będzie przechowywany w zmiennej return_code, która będzie wynosić zero, jeśli polecenie 
się powiedzie, i wartość różną od zera, jeśli polecenie się nie powiedzie. subprocess.call() jest przydatna,
gdy chcesz uruchomić polecenie i sprawdzić kod powrotu, ale nie musisz przechwytywać danych wyjściowych.
"""   

if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))