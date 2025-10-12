"""
'r'  - plik otwarty do odczytu (read)
'w' - plik otwarty do zapisu (write), przed zapisem zawartość pliku jest usuwana
'a' - plik otwarty do zapisu, dodaje nową treść na końcu pliku, nie usuwa starej (append)
Przykład:
f = open(filepath, "r", encoding="utf-8")
    operacje na pliku
f.close()  
"""

def pobierzCalyPlik(name):
    file = open(name,"r" ,encoding="utf-8")
    tmp = file.read() # odczyt całego pliku; odczyt pierszych 8 znaków: file.read(8)
    print(tmp)
    file.close()

def pobierzLiniaPoLini(name):
    f = open(name)
    for line in f:
        print (line)
    f.close()

def pobierzLiniaPoLiniReadLines(name):
    f=open(name)
    lines = f.readlines()
    print(lines)
    f.close()

def pobierzLinie(name):
    f=open(name)
    linia = f.readline()
    print("Pierwsza linia:", linia)
    linia = f.readline()
    print("Druga linia:", linia)
    f.close()
    
def pobierzDoListy(name):
    L = [linia.strip()  for linia in open(name)]
    print (L)

def pobierzZnakPoznaku(name):
    with open(name) as f:
        znak = f.read(1)
        while znak:
            print (znak)
            znak = f.read(1)

def pobierzSeek(name):
    f = open(name, "r")
    f.seek(20)            # Ustawia pozycję na 20 znaku(bajcie)
    print(f.tell())       # potwierdza pozycję kursora
    print(f.readline())   # odczytuje linię od 20 znaku do jej końca
    f.close()

"""
Explanation:

File is opened in binary mode ('rb').
seek(-10, 2) moves 10 bytes before the end of the file.
readline() reads from that point to the end.
Output is decoded from binary to string.

f = open("data.txt", "rb")
f.seek(-10, 2)
print(f.tell())
print(f.readline().decode('utf-8'))

f.close()
"""


"""
Zapis do pliku:

f = open(filepath, "w")
f.write("Dane")
f.write("dane2")

a jescze lepiej:
with open(filepath, "w") as f:
	f.write("Zapisujemy do pliku\n")

Odczyt i zapis do 2 plików:
with open('read_from.txt', 'r') as reader, open('write_to.txt', 'w') as writer:
    text = reader.read()
    writer.write(text)
"""

def main(args):
    filename = "dane.txt"  # ścieżka względna lub ścieżka absolutna(bezwzgledna) np: "E:\blog\dane.txt"
    pobierzCalyPlik(filename)
    pobierzLiniaPoLini(filename)
    pobierzDoListy(filename)
    pobierzZnakPoznaku(filename)
    pobierzLinie(filename)
    pobierzLiniaPoLiniReadLines(filename)
    pobierzSeek(filename)

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
