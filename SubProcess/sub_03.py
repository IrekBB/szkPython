"""
Kod pythona uruchomiony bezpośrednio z funkcji run
Na liście argumentów pierwszy element sys.executable dynamicznie określa ścieżkę bieżącego interpretera Pythona.
Zapewnia to spójność z działającym procesem i pozwala uniknąć zakodowanych na stałe ścieżek, takich jak „C:/…”. 
Drugi element, „-c”, uruchamia następujący ciąg jako kod Pythona zamiast skryptu. Zawsze dołączaj import sys, aby 
uzyskać dostęp do pliku sys.executable.
"""

def main(args):
    result = subprocess.run([sys.executable, "-c", "print('Kod pythona uruchomiony bezpośrednio z funkcji  subprocess.run().')"], 
                            capture_output = True, text = True)
    print(result.stdout)

if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))