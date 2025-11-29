"""
Uruchamianie skryptów w pythonie:

"""

def main(args):
    print("---------- Dodawanie ---------------")
    x = input("x=")
    y = input ("y=")
    result = subprocess.run(['python', 'add.py', x, y],capture_output=True, text=True)
    print (result.stdout)
    print ("--------- Odejmowanie -------------")
    try:
        result1 = subprocess.run([sys.executable, "d.py", x, y], capture_output=True, text=True, check=True)
        print(result1.stdout)
    except subprocess.CalledProcessError as e:
        print ("Błąd dzielenia przez zero")
    



if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))