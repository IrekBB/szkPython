# -*- coding: utf-8 -*-
class Wyrazenie:    # Drzewo binarne zapamietujące wyrażenie arytmetyczne
    def __init__(self):
        self.val = 0   # Wartość bez znaczenia (będzie nadpisana)
        self.op = '0'  # Operator bez znaczenia (będzie nadpisany)
        self.lewy = None
        self.prawy = None # lewy,prawy - potomkowie w�z�a pe�ni�cecego funkcje operatora

    def pisz_infix(self):   # postać infiksowa wyrażenia
        if self.op =='0':    # wartość liczbowa
            print(str(self.val), end=" ")
        else:
            print("(", end=" ")
            self.lewy.pisz_infix()
            print (self.op, end=" ")
            self.prawy.pisz_infix()
            print(")", end = " ")

    def pisz_prefix(self):   # postać prefiksowa wyrażenia
        if self.op=="0": # Wartość liczbowa
            print ( str(self.val), end =" ")
        else:
            print (self.op + " ", end=" ")
            self.lewy.pisz_prefix()
            self.prawy.pisz_prefix()
    
    def poprawne(self):	# Czy wyrażenie jest poprawne składniowo?
            if self.op=='0':
                return True		# Według naszej konwencji jest to liczba, więc akceptujemy
            if self.op in ['+', '-', '*', ':', '/']:	# Sprawdzimy teraz operator, czy jest nam znany
                return (self.lewy).poprawne() and (self.prawy).poprawne()
            else:
                return False	# Błąd,  nieznany operator lub inny błąd
	
    def oblicz(self):
           if self.poprawne():  # Wyrażenie poprawne?
                if (self.op=='0'):
                    return self.val	# Pojedyncza wartość
                elif self.op=='+':
                    return (self.lewy).oblicz()+(self.prawy).oblicz()
                elif self.op=='-':
                    return (self.lewy).oblicz()-(self.prawy).oblicz()
                elif self.op=='*':
                    return (self.lewy).oblicz()*(self.prawy).oblicz()
                elif (self.op==':' or self.op=='/'):
                    if (self.prawy).oblicz()!= 0:
                        return (self.lewy).oblicz() / (self.prawy).oblicz()
                    else:
                        print("\nDzielenie przez zero!")
                        return -1	# Uproszczona sygnalizacja błędów
           else:
               print("Błąd składni")
               return -1	# Uproszczona sygnalizacja błędów
            
        
if __name__=="__main__":
    print ("To jest moduł! Wykonaj plik  WyrArtBinMain.py")

