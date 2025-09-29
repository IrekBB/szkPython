def modulo(liczba,dzielnik):
    wynik=0
    for i in range(len(liczba)):
        wynik = wynik * 10 + int(liczba[i])
        wynik = wynik%dzielnik
    return wynik

def main(args):
    liczba = input("Podaj liczbę: ")
    dzielnik = eval(input("Podaj dzielnik modulo: "))
    print(f"{liczba} mod {dzielnik}={modulo(liczba,dzielnik)}")


if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))






