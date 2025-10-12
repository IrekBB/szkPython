from MojeModuly import Lista2Kier as l

def main(args):
    lista =  l.Lista2Kier()
    lista.wstaw("A", 12)
    lista.wstaw("B", 34)
    lista.wstaw("C", 34)
    lista.wstaw("D", 55)
    lista.wstaw("E", 67)
    lista.wypiszWprzod("Lista od przodu:")
    lista.wypiszWstecz("Lista od tyłu:")
    lista.usun("A")
    lista.wypiszWprzod("Lista od początku:")


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
