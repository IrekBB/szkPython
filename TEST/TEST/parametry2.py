#  * w pierwszym kroku sprawdzamy liczbę parametrów, jesli jest ona 
# błędna to kończymy działanie programu
#  ** w drugim kroku sprawdzamy poprawność wartości parametrów (np. składnię, zakresy liczbowe)
import sys

def main(args):
    if len(args) !=  4:
        print ("""Wymagane użycie trzech parametrów:
               <plik wejściowy.csv> <plik wyjściowy.csv> <N>, 
               gdzie N jest liczbą w zakresie 1-10""")
        print ("Do widzenia!")
        sys.exit()
    # 'find' - metoda klasy <str>, zwraca iddeks wystąpienia pierwszego napisu's'
    # w badanym ciągu znaków lub wartość  -1 w przeciwnym razie
    par1 = args[1].find(".csv") != -1
    par2 = args[2].find(".csv") != -1
    val = args[3]
    par3 = val.isdigit() and 1 <= int(val) <= 10
    if not (par1 and par2 and par3):
        print ("Jeden z podanych parametrów jest błędny")
        print("Do widzenia")
    print ("O to lista parametrów: ", args[1:])

if __name__ == "__main__":
    sys.exit(main(sys.argv))