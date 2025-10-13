import sys
def main(args):
    # Stara metoda obecnie niepolecana
    import os
    os.system(' "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" ')
    print ("Zakończono zewnętrzny proces - program MS Edge")

    import subprocess # Zalecana metoda
    try:
        subprocess.call("C:/Program Files (x86)/Notepad++/notepad++.exe") # Wywołanie blokujące
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)
    finally:
        print ("Zakończono zewnętrzny proces - program Notepad.exe")

    subprocess.Popen("C:/Windows/System32/calc.exe") # Wywołanie nieblokujące
    print ("W tle działa uruchomiony, zewnetrzny proces - program calc.exe")
    input ("Nacisnij klawisz ENTER")
    print ("Do wiszenia")



if __name__ == "__main__":
    sys.exit(main(sys.argv))