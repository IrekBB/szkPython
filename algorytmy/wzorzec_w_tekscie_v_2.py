def czy_wzorzec(wzorzec, tekst):
    for i in range(len(tekst)-len(wzorzec) + 1):
        if tekst[i:len(wzorzec)+i]==wzorzec:
            return True
    return False


def main(args):
    wzorzec = input('wzorzec: ')
    tekst = input('tekst: ')
    if czy_wzorzec(wzorzec, tekst):
        print (f'Wzorzec {wzorzec} występuje w tekście {tekst}')
    else:
        print (f'Brak wzorca {wzorzec} w tekście {tekst}')
    

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
