"""
python subprocess check_output
check_output to funkcja w module podprocesu, podobna do run(), ale zwraca tylko standardowe wyjście polecenia
i zgłasza wyjątek CalledProcessError, jeśli kod powrotu jest różny od zera. Funkcja check_output() przyjmuje te
same argumenty co run(), w tym args (polecenie do uruchomienia) i argumenty opcjonalne, takie jak stdin, stderr,
Shell, cwd i env. Zwraca standardowe wyjście polecenia jako obiekt bajtowy lub ciąg znaków (jeśli tekst=True).
Zgłasza CalledProcessError, jeśli polecenie się nie powiedzie (niezerowy status wyjścia). 
Uwaga: Domyślnie check_output() przechwytuje tylko standardowe wyjście. Aby uwzględnić stderr w wynikach, 
jawnie przekieruj je za pomocą stderr=subprocess.STDOUT.
"""
def main(args):
    try:
        output = subprocess.check_output([sys.executable, "--version"], text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")

if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))
