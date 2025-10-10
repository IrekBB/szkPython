RMAX = 20


def H1(s):
    tmp = 5381
    for znak in s:
        tmp = ((tmp << 5) + tmp) + ord(znak)
    return tmp

def szukaj(T, klucz):
    print("Szukam...")
    pos = hash(klucz) % RMAX
    while (T[pos] != None) and (T[pos][0] != klucz):
        pos = (pos+1) % RMAX
    return T[pos]    

class  Element:
    def __init__(self, pWiek, pNazwisko):
        self.wiek = pWiek 
        self.nazwisko = pNazwisko
    
    def __hash__(self):     # Spersonalizowana metoda hash()
        return hash( (self.wiek, self.nazwisko) )
    
    def __eq__(self, o2):
        return self.wiek == o2.wiek and self.nazwisko == o2.nazwisko
    
    def __str__(self):
        return str(self.wiek) + str(self.nazwisko)



if __name__=="__main__":
    print("* To jest moduł. Można go wywołać z poziomu skryptu MainHash *")
