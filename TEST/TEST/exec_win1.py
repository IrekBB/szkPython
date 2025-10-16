import sys
import subprocess

def main(args):
    subprocess.run(["dir", "E:/Users/opiekun/Documents/SzkPython"])  # doesn't capture output
    subprocess.run(["dir", "E:/Users/opiekun/Documents/SzkPython"], capture_output=True)

    prog = subprocess.Popen("date", stdout=subprocess.PIPE, shell = True)
    (wynik, err) = prog.communicate()
    print (f"Dziś jest: {wynik}")

    prog = subprocess.run(["python","E:/Users/opiekun/Documents/szkPython/TEST/funkcje.py"])

    with subprocess.Popen(["dir", "E:/Users/opiekun/Documents/SzkPython"], stdout=subprocess.PIPE, shell=True) as proc:
        out=proc.stdout.readlines()

    print(out)

    

if __name__ == "__main__":
    sys.exit(main(sys.argv))