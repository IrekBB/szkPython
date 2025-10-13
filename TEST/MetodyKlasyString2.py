def main(args):
     s = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
     print(s)
     print(s.replace("wood","Drewno",2)) #Zamienia wystapienie ciągu old na new tyle razy, ile okreslono to
     # w parametrze count (jeśli go nie podasz, zostaną zatapione wszystkie znalezione wystąpienia)
     print (s.split("woodchuck")) # Zwraca listę słów w napisie wejściowym przy założeniu, że te umowne
     # "słowa" sa odzielone prez separator, domyslnie separatorem jest spacja; parametr opcjonalny maxsplit
     # określa maksymalną liczbę podziałów
     print (s.split(" ",3))
     print (s.rsplit(" ", 3))  # analizuje napis od prawej! strony


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))