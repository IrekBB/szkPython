"""
 dekorator — funkcja, która będzie zwracała przekazany jej obiekt
 
 def dekorator(obj):
    return obj

 Opatrzmy teraz przykładową funkcję naszym nowo utworzonym dekoratorem:

 @dekorator
 def funkcja():
    print("hello")

Zapis ze znakiem @ przed funkcją to syntactic sugar i jest on równoważny następującemu zapisowi:
funkcja = dekorator(funkcja)

    
"""


import sys

def inna_funkcja():
    print("inna funkcja")

def dekorator(obj):
    return inna_funkcja

@dekorator             # syntactic sugar
def funkcja():
    print("hello")


"""
operacje dokonywane są tutaj na nazwach. Nazwa funkcja przestaje wskazywać na obiekt reprezentujący naszą
przykładową funkcję i od tego momentu wskazuje na obiekt zwrócony przez dekorator. W powyższym przypadku 
jest to ten sam obiekt, ale nietrudno jest sobie wyobrazić funkcję dekoratora w zmienionej postaci — zwracającej inny obiekt:

"""

def main(args):
    funkcja()

if __name__ =="__main__":
    sys.exit(main(sys.argv))