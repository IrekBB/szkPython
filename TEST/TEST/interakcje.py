def main(args):
    while True:
        try:
            imie = input ("Podaj imię: ")
            wiek = int (input("Ile masz lat? "))
            break
        except (ValueError, TypeError):
            print ("wiek musi być liczbą. Próbuj dalej... ")
    
    print (f"Imię: {imie}, wiek: {wiek}")
    
    input ("Naciśnij dowolny klawisz ...")
    print ("Do widzenia!")

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
