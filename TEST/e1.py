import easygui
import sys

def main(args):
    input ("Naciśnij klawisz Enter i obserwuj komunikaty wyświetlane w konsoli tekstowej:")
    odp1 = easygui.ynbox("Czy lubisz Pythona?", "Pytanie na śniadanie", ("Tak","Nie"))
    print ("Odpowiedż:", odp1)
    easygui.msgbox("Atak Daleków!", "Dr Who pomocy!")
    odp2=easygui.buttonbox("Wybierz ulubiony język programowania", "Ankieta językowa",("C++", "Pythona", "Java"))
    print ("Wybrano:", odp2)
if __name__=="__main__":
    sys.exit(main(sys.argv))