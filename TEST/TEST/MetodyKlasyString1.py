def main(args):
    s = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
    print(s.count("wood"))  # zwraca ilość wystapień podciągu w ciągu s
    print(s.count("wood", 0, 15))  # zakres od 0 do 15 znaku
    print(s.endswith("?")) # zwraca True lub False, w zalezności od tego czy napis kończy się suffixem czy też nie
                           # parametry opcjonalne start i end (zakres - jak wyżej)
    print(s.startswith('Howdy'))  # True lub False, czy zaczyna się lub nie od prefixu
                                  # parametry opcjonalne start i end
    s = "Programiści lubią Pythona"
    print (s)
    print (s.find("lubią"))  # zwraca indeks pierwszego wystapienia  podciągu, lub -1 w przeciwnym razie
    print (s.find("kochają"))  # dodatkowe opcjonalne parametry to start i end
    s = "Programiści lubią Pythona  Programiści lubią Pythona"
    print (s.rfind("lubią")) # podobne do find, ale zwraca najwyższy odszukany indeks lub -1
                             # opcjonalne parametry to start i end
    print (s.index("lubią")) # zwraca indeks pierwszego wystapienia podciągu lub zgłasza wyjątek ValueError
                             # parametry start i end (zakres przeszukiwania)
    try:
        print (s.index("kochają"))
    except ValueError:
        print ("Podciągu 'kochają' nie odnaleziono w napisie:", s)
    finally:
        print ("\n'rindex(sub)' - działa podobnie jak index, ale zwraca najwyższy odszukany indeks\n"
        + " lub zgłasza wyjątek ValueError, jeśli nie zostanie odnalezione. Parametry: zasięg przeszukiwania ")



if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
