"""
Użycie argumentu check
Argument check (opcjonalny) jest wartością logiczną, która sprawdza czy funkcja run powinna kontrolować
kod powrotu zwracany skutkiem jej wywołania. 

Gdy check jest ustawiony na True, funkcja sprawdzi kod powrotu polecenia i zgłosi wyjątek CalledProcessError
(jeśli kod powrotu jest różny od zera). Zwracany wyjątek będzie posiadał poniższe atrybuty:  kod powrotu, stdout, stderr i kod polecenia.

Gdy check ma wartość False (domyślnie), funkcja nie sprawdza kodu powrotu i nie zgłosi wyjątku, nawet jeśli wykonanie polecenia 
nie powiedzie się.
"""

def main(args):
    result = subprocess.run(["python", "file_donot_exist.py"], capture_output=True, text=True, check=True)

    print(result.stdout)
    print(result.stderr)
"""
Gdy zamienimy wartość check na False:
zauważ, że wykonanie polecenia nie powiodło się, ponieważ plik file_donot_exist.py nie istnieje. 
W przeciwieństwie do ustawienia check=True, proces nie zakończy się niepowodzeniem; zamiast tego pojawi się komunikat o błędzie na stdout.
"""

if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))