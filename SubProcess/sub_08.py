"""
Python Subprocess Pipe

Moduł subprocess  języka Python umożliwia tworzenie procesów potomnych i interakcję z nimi.
Podprocesy, można między innymi wykorzystać do uruchamiania innych programów lub poleceń.
Proces nadrzędny i jego podprocesy komunikują się ze sobą za pomocą tzw. potoków (Pipe).

Potok to jednokierunkowy kanał komunikacyjny, który łączy standardowe wyjście jednego procesu ze standardowym
wejściem innego procesu. Potok może łączyć wyjście jednego polecenia z wejściem innego, umożliwiając
wykorzystanie wyniku pierwszego polecenia jako wejścia drugiego polecenia.

Potoki można tworzyć za pomocą modułu subprocess z klasą Popen, określając argument stdout lub stdin jako subprocess.PIPE. 


"""
def main(args):
   ls_process = subprocess.Popen(["python", "--help"],stdout=subprocess.PIPE, text=True)
   
   grep_process = subprocess.Popen(
   ["findstr", "cmd"],
    stdin=ls_process.stdout,
    stdout=subprocess.PIPE,
    text=True
    )
   ls_process.stdout.close()  # POSIX-only: prevents deadlocks by closing the pipe
   output, error = grep_process.communicate()

   print(output)
   print(error)
 
if __name__=="__main__":
    import sys
    import subprocess
    sys.exit(main(sys.argv))