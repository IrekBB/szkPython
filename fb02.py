slownik={}
slownik[1]='jeden'
slownik[2]='dwa'

pracownicy={
    'imie':'Janusz',
    'nazwisko':'Minotaur',
    'zawód':'inżynier',
}

print ('******************* klucze ***************')
for key in pracownicy:
    print (key)

print ('************* klucz / wartość********')
for key, value in pracownicy.items():
    print (key,"=>",value)

print ('************* klucze **************')
for key in pracownicy.keys():
    print (key)
print ('******************  wartości ******************')
for value in pracownicy.values():
    print (value)

pracownicy['wiek']=35

print ('*********** klucz/ wartość **************')
for key, value in pracownicy.items():
    print (key,"=>",value)

# .del , .clear 


p1={
    'imie':'Janusz',
    'nazwisko':'Minotaur',
    'zawód':'inżynier',
}

p2={
    'imie':'Jarosław',
    'nazwisko':'Kędzior',
    'zawód':'nauczyciel',
}

print ('***************** Lista pracowników ****************')
lista_p=[p1,p2]


for e in lista_p:
    print (e['imie'],' ', e['nazwisko'],' ', e['zawód'])
