import sys
import subprocess
import shlex

def main(args):
    command_line = input()      # zapis postaci dir e:\\Users\\opiekun\\Documents\\SzkPython\\Test
    args = shlex.split(command_line)
    print(args)
    prog = subprocess.Popen(args, stdout=subprocess.PIPE, shell = True)
    (wynik, err) = prog.communicate()
    print(f"Surowy wynik komendy \'dir\':\n {wynik}")
    tmp = str(wynik)
    tmp = tmp.lstrip('b\'')
    print ("#########################################################################")
    print ("Wynik pozbawiony prefiksu:\n", wynik)
    print ("#########################################################################")
    print ("Tak wygląda lista plików wykrytych w folderze:" )
    lista_plikow_all = tmp.split()
    lista_plikow_all_spacja=list()
    for s in lista_plikow_all:
        if s !="":
            lista_plikow_all_spacja.append(s)
    
    print (lista_plikow_all_spacja)
    print ("#########################################################################")
    lista_plikow_py=list()
    for s in lista_plikow_all_spacja:
        if  s.find(".py")  != -1:
             lista_plikow_py.append(s)
    
    lista_niemal_final=list()
    for s in lista_plikow_py:
        if  s.split("\\")  != -1:
             lista_niemal_final.append(s)

    lista_final=list()      
    print ("Drukujemy przed listę plików Pythona:\n", lista_niemal_final)
    print("########################################################################")  
    for s in lista_niemal_final:
        tempL = s.split("\\")
        lista_final.append(tempL[0])
    print (*sorted(lista_final,reverse=True))
    


if __name__=="__main__":
    sys.exit(main(sys.argv))