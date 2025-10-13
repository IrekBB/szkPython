def main(args):
    s = "Ala ma kota i psa: 4 psy i 2 koty."  # to nie jest alfanumeryk (litery lub cyfry)
    s1 = "AlaMaKotaIPsa4psyI2Koty" # a to jest alfanumeric
    if s1.isalnum():
        print ("Napis składa się z cyfr i liter alfabetu")
    else:
        print ("To nie jest napis alfanumeryczny")

    if s1.isalpha():   # sprawdza czy tekst skkłada się z samych znaków alfabetu
        print ("Same litery alfabetu.")
    else:
        print ("Nie tylko same litery alfabetu.")
    
    if s.isascii():  # True - jeśli znaki sa z kodu ASCII (U+0000 - U007F) lub pusty
        print("Znaki są zgodne z kodem ASCII ")
    else:
        print ("Znaki niezgodne z kodem ASCII")
    
    liczba = 12390
    s3 = str(liczba)
    if s3.isdigit():              # Zwraca True jeśli napis składa się wyłącznie z cyfr (0-9) i nie jest pusty
        print ("Wyłącznie cyfry")
    else:
        print("Nie tylko cyfry")
    
    s4 = "małe litery w napisie. nie ma dużych ."    # małe ale jest kropka na końcu
    if s3.islower():  # True - jeśli wyłącznie małe litery
        print ("Same małe litery w napisie.")
    else:
        print ("Jakaś duża lub cyfra.")

    s5 = "ALAMAKOTA"
    if s5.isupper():      # Same duże litery w tekście
        print ("Same duże litery w tekście.")
    else:
        print ("Jest jakiś dodatkowy znak (-znaki), które nie są duzymi literami.")
    
    s6 = "      "
    if s6.isspace():   # True, jesli napis składa się wyłącznie ze spacji i nie jest pusty
        print ("Same spacje.")
    else:
        print ("Spacje i nie tylko")

    s7="To Jest Tytuł"  
    if s7.istitle():    # True jesli każda pierwsza litera wyrazu jest duża (pozostałe litery wyrazu są małe)
        print ("Styl Tytułowy")
    else:
        print ("To nie jest styl tytułowy")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))