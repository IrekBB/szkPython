def zawiera(wyraz, zdanie):
    print(f"Szukam '{wyraz}' w '{zdanie}' ")
    n = len(wyraz)
    if n > len(zdanie):
        print ("Poszukiwane słowo jest dłuższe niż zdanie...")
        return False
    wyraz_lst = list(wyraz)
    zdanie_lst = list(zdanie)
    print (len(zdanie_lst), "  ",zdanie_lst)
    for e in wyraz_lst:
        try:
            zdanie_lst.remove(e)
        except ValueError:
            pass
    print(len(zdanie_lst), "  ", zdanie_lst)
    print(len(wyraz_lst), "  ", wyraz_lst)
    return len(zdanie) - n == len(zdanie_lst)

def main(args):
    print (zawiera("Bramka","Bronek alergicznie nie znosił makaronu z kaszą"))
    print (zawiera("Kia","Salon samochodów Renault i Nissan"))

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
