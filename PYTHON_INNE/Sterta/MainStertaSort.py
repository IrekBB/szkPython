def main(args):
    tab = [40, 2, 1, 6, 18, 29, 29, 32, 23, 34, 91, 45, 6]
    print(tab)
    sterta = s.Sterta(len(tab))
    for element in tab:
        sterta.wstaw(element)
    for i in range(len(tab)-1, -1, -1):
        tab[i] = sterta.obsluz()
    print(tab)

if __name__=="__main__":
    import sys
    from MojeTypy  import Sterta as s
    sys.exit(main(sys.argv))
