def main(args):
    tab1 = [1, 2, 6, 111111118, 18, 20, 23, 29, 32, 34, 40, 41, 100 ]
    for i in range(0, len(tab1)):
        print (f"t[{i}] = {tab1[i]}", end=" ")
    print()
    print (f"Szukam 23, wynik: {s.szukajBin(tab1, 23)}")
    print (f"Szukam 3, wynik: {s.szukajBin(tab1, 3)}")


if __name__ == "__main__":
    from MojeTypy import szukaj as s
    import sys
    sys.exit(main(sys.argv)) 