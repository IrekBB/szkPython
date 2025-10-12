# -*- coding: utf-8 -*-
def main(args):

    wart = [2, 3, 0, 7, 9, 0, 0, 12.5, 0]
    oper = ['0', '0', '+', '0', '0', '*', '+', '0'  ,'*']

    s=list()	# Lista użyta jako stos roboczy przeznaczony do przechowywania obiektów klasy 'Wyrazenie'
    w=None	# Puste wyrazenie

    for i in range( len(wart) ):
        w=W.Wyrazenie()
        if oper[i] in ['+', '-', '*', ':', '/']:
            w.op=oper[i]
        else:
            w.op='0'	# Umowna konwencja oznaczająca wartość, a nie operator
            w.val=wart[i]
        w.lewy  = None
        w.prawy = None

        if oper[i] in ['+', '-', '*', ':', '/']:
            l1=W.Wyrazenie()
            p1=W.Wyrazenie()
            l1=s.pop()
            p1=s.pop()
            w.lewy =l1	# "Podwiązanie" pod węzeł x
            w.prawy=p1; # "Podwiązanie" pod węzeł x
        s.append(w)

    print("Prefiks: ")
    w.pisz_prefix();
    print("\nWynik: " + str(w.oblicz()) )
    print("Infiks: ")
    w.pisz_infix()


if __name__ == "__main__":
    print ("żść")
    import sys
    from MojeTypy import Wyrazenia as W
    sys.exit(main(sys.argv))
