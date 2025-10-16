def main(args):
    nowyplik = "output.txt"
    print (f"Zapis do pliku tekstowego: {nowyplik}")
    plik_out = open(nowyplik,"w")
    print ("zapisuję do ", nowyplik," zawartość: 'Nowy wiersz 1', 'Nowy wiersz 2', 'Nowy wiersz 3'")
    plik_out.write("Nowy wiersz 1\n")
    plik_out.write("Nowy wiersz 2\n")
    plik_out.write("Nowy wiersz 3\n")
    """
    Szybszy zapis:
    lst = ['Nowy wiersz 1\n', 'Nowy wiersz 2\n', 'Nowy wiersz 3\n']
    plik_out.writelines(lst)
    """
    plik_out.close()
    input (f"Plik {nowyplik} został utworzony na lub nadpisany na dysku - sprawdź jego zawartość, a następnie nacisnij Enter, aby kontynuować") 

    print(f"Otwieram plik: {nowyplik} do odczytu i zapisu")
    plik_in_out = open(nowyplik, "r+")
    print ("Czytam wiersz 1.: ", plik_in_out.readline(), end="")
    print ("Czytam wiersz 2.: ", plik_in_out.readline(), end="")
    print("Zapisuję do ", nowyplik," nowy napis: 'THE DOORS:'")
    plik_in_out.write("THE DOORS:")
    print ("Dopisuję do ", nowyplik," nowy napis: 'This is the end, my only friend...' oraz znak nowej linii")
    plik_in_out.write("This is the end, my only friend...\n")
    # w tym miejscu nic niema bo wskaźnik pliku ustawiony jest na koniec, po ostatnim zapisie, chyba, że plik_in_out.seek(0,0)
    print("Czytam dalej:", plik_in_out.readline(), end="")
    plik_in_out.close()
    print("\nOtwietramy ponownie plik i sprawdzamy zawartość")
    plik_in = open(nowyplik,"r")
    print (plik_in.read())
    plik_in.close()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
