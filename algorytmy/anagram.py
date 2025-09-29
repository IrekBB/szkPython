def anagram(a,b):
    dla, dlb = len(a), len(b)
    if dla != dlb: return False
    zbior = set(a)
    slownik={}
    for el in zbior:    # zerowanie słownika
        slownik[el]=0

    for znak in a:      # wypełnianie słownika
        for key in slownik.keys():
            if key==znak: slownik[key]=slownik[key] + 1

    for znak in b:
        for key in slownik.keys():
            if key == znak: slownik[key] = slownik[key]-1

   
    for key in slownik.keys():
        if slownik[key]!=0: return False

    return True
        
        
        
    
    
def main():
    a = input('słowo: ')
    b = input('czy anagram? ')
    if anagram(a,b): print (f'{b} jest anagramem  słowa {a}.')
    else: print (f'{b} nie jest anagramem słowa {b}.')
    

if __name__ == '__main__':
  import sys
  sys.exit(main())
    
