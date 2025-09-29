def szukaj(tab, x):     # Szukaj x w tablicy (tab)
    if len(tab) == 0:
        return 0
    i = 0
    while i < len(tab):
        if tab[i] == x:
            break
        else:
            i = i + 1
    return i

class Element: # pewien rekord danych
    def __init__(self, pImie, pWiek):
        self.imie = pImie
        self.wiek = pWiek

def porownaj_wiek(obj, pWiek):
    if type(obj) != Element:
        print ("Nieprwidłowy obiekt, uciekam....")
        return False
    if obj.wiek == pWiek:
        return True
    else:
        return False

def porownaj_imiona(obj, pImie):
    if type(obj) != Element:
        print ("Nieprwidłowy obiekt, uciekam....")
        return False
    if obj.imie == pImie:
        return True
    else:
        return False
    
def szukajGen(tab, x, porownywarka): # Szukaj x w tablicy; zmienna 'porownywarka'
                                     # jest referenja do funkcji
    if len(tab)==0:
        return -1
    i = 0
    while i < len(tab):
        if porownywarka(tab[i], x):
            break
        else:
            i=i+1
    return i

def szukajBin(tab, x):
    left = 0
    right = len(tab) - 1
    mid = 0
    znaleziono = False
    while (left<=right) and (not znaleziono):
        mid = (left + right)//2  # Dzielenie całkowite
        if tab[mid] == x:
            znaleziono =  True
        else:
            if tab[mid] < x:
                left = mid + 1
            else:
                right = mid -1
    if znaleziono == True:
        return mid
    else:
        return -1

if __name__=="__main__":
    print("* To jest moduł. Można go wywołać ze skryptu MainSzukaj, MainSzukajGen lub MainszukajBin *")
