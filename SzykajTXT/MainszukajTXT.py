def main(args):
    tekst = input("Przeszukiwany tekst: ")
    wzorzec = input ("Wzorzec: ")
    print ("*** Metoda  brute force ***")
    pozycja_wzorca = s.szukaj(wzorzec, tekst) 
    if pozycja_wzorca == -1:
        print (f"Wzorca: '{wzorzec}' w tekście: '{tekst}' nie odnaleziono.")
    else:
        print (f"Wzorzec '{wzorzec}' w tekscie: '{tekst}' występuje na pozycji: {pozycja_wzorca}")

if __name__=="__main__":
    import sys
    from MojeTypy import szukaj as s
    sys.exit(main(sys.argv))

