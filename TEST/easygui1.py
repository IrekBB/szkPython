import easygui
import sys

def main(args):
    print ("***   Podstawowe składowe easygui   ***")
    print ("1. Okno komunikatu easygui.msgbox")
    msg = "Komunikat"
    tytul = "Tytuł okna"
    ok_button = "przycisk OK"
    easygui.msgbox(msg, tytul, ok_button)  # najprostsze wywołanie: 'easygui.msgbox(msg)'
    print ("2. Okno kontynuacji easygui.ccbox/ynbox")
    msg = "Kontynujemy?"
    title = "Prośba o ptwierdzenie"
    pytania = ["Tak", "Anuluj"]
    if easygui.ccbox(msg, title, pytania):
        print ("Potwierdziłeś kontynuacje")
    else:
        print ("Do widzenia")
    print ("3. Okno wyboru easygui.buttonbox")
    title = "Jakie miasto jest stolicą Hiszpanii?"
    pytania = ["Monte Video", "Lizbona","Madryt", "Buenos Aires"]
    odp = easygui.buttonbox("Wybierz dobrze!", title, pytania, image="moje-logo.gif")
    if odp=="Madryt":
        easygui.msgbox("Tak, dobrze! Stolicą Hiszpanii jest Madryt","Miasta świata","OK")
    else:
        easygui.msgbox("To błędna odpowiedź! Stolicą Hiszpanii jest Madryt","Miasta świata","OK")
    print ("4. Lista wyboru easygui.choicebox")
    print("***   Lista pojedynczego wyboru   ***")
    title = "Scenariusze"
    pytanie = "Prawdopodobieństwo wyrzucenia resztki w jednokrotnum rzucie moneta wynosi:"
    listawyboru = ["1/2", "1/3 bo może spaść na sztorc", "1/4","żadne z powyższych"]
    odp = easygui.choicebox(pytanie, title,listawyboru, preselect=0)
    if odp == listawyboru[0]:
        easygui.msgbox("OK! To poprawny wybór:" + str(odp), "Okno odpowiedzi","OK")
    else:
        easygui.msgbox("Żle! Poprawny wybór to:" + str(listawyboru[0]), "Okno odpowiedzi","OK")
    print ("5. Lista wyboru easygui.multchoicebox")
    print("***   Lista wielokrotnego wyboru   ***")
    title = "Scenariusze"
    pytanie="Wybierz jeden lub więcej scenariuszy do uruchomienia"
    listawyboru=["Test-run1", "Test-run2", "Test-run3","Test-run4", "Test-run5"]
    odp = easygui.multchoicebox(pytanie, title, listawyboru, preselect=0)
    easygui.msgbox("Wybrano:"+ str(odp))

if __name__=="__main__":
    sys.exit(main(sys.argv))
