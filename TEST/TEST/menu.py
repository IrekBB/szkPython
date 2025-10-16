def menu():
    print (""" 
           *** Dostępne opcje ***
           q - Wyjście
           1 - Uruchominie testów
           2 - Analiza logów
           3 - Przerwa na kawę""")
    opcja = input ("wybierz opcję: ")
    print()
    return opcja




def main(args):
    opcja = str() 
    while opcja != "q":
        opcja = menu()
        if opcja=="q":
            print ("Do widzenia")
        elif opcja == "1":
            print ("Wybrano: '1 - Uruchomienie testów'")
        elif opcja=="2":
            print ("wybrano: '2. Analiza logów' ")
        elif opcja =="3":
            print ("Wybrano: '3. Przerwa na kawę' ")
        else:  # błędna opcja
            print (f"Niepoprawna opcja {opcja}, spróbuj ponownie!")

    input ("\n\nNaciśnij klawisz Enter")

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))