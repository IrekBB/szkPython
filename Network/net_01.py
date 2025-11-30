"""
Naszą funkcję wywołujemy ze zwykłego bloku Pythona __main__. W czasie wykonywania Python 
przypisuje wartości niektórym zmiennym wewnętrznym, takim jak __name__. W tym przypadku __name__ 
odnosi się do nazwy procesu wywołującego. Podczas uruchamiania tego skryptu z wiersza poleceń,
jak pokazano w poniższym poleceniu, nazwą będzie __main__. Ale będzie inaczej, jeśli moduł zostanie
zaimportowany z innego skryptu. Oznacza to, że gdy moduł zostanie wywołany z linii poleceń, 
automatycznie uruchomi naszą funkcję print_machine_info; jednakże w przypadku osobnego importu 
użytkownik będzie musiał jawnie wywołać tę funkcję
"""
def print_machine_info():
    host_name = socket.gethostname()
    ip_adress = socket.gethostbyname(host_name)
    print ("Host name: %s" %host_name)
    print ("IP adress: %s" %ip_adress )
"""
Pierwsza funkcja nie przyjmuje żadnego parametru i zwraca nazwę bieżącego lub lokalnego hosta.
Druga funkcja pobiera pojedynczy parametr nazwy hosta i zwraca jego adres IP
"""

def main(args):
    print_machine_info()
    


if __name__=="__main__":
    import sys
    import socket
    sys.exit(main(sys.argv)) 