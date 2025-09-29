"""
Szyfry przestawieniowe dokonują przestawienia znaków w tekście.
Tekst zaszyfrowany jest permutacją tekstu jawnego, tzn. zawiera wszystkie znaki
tekstu jawnego, jednak ustawione w innej kolejności.
Operacja taka nosi nazwę TRANSPOZYCJI.
"""
def TR_kod(tekst, jump):
    tekst = list(tekst)
    for i in range(0, len(tekst)-1, jump):
        tekst[i], tekst[i + 1] = tekst[i + 1], tekst[i]
    return "".join(tekst)

def TR_dekod(tekst, jump):
    tekst = list(tekst)
    for i in range(0, len(tekst)-1, jump):
        tekst[i], tekst[i + 1] = tekst[i + 1], tekst[i]
    return "".join(tekst)
    


def main(args):
    txt = "SzyfrTranspozycyjny"
    kod = TR_kod(txt,3)
    print(kod)
    print(TR_dekod(kod,3))
    
    

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
    
