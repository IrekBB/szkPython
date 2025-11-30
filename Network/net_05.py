"""
Converting integers to and from host to network byte order

Jeśli kiedykolwiek będziesz musiał napisać aplikację sieciową niskiego poziomu, może okazać sie konieczna 
obsługa transmisji danych niskiego poziomu  pomiędzy dwiema maszynami. Ta operacja wymaga  
konwersji danych z rodzimego systemu operacyjnego hosta do formatu sieciowego i odwrotnie. 
Dzieje się tak, ponieważ każdy z nich ma swoją własną specyficzną reprezentację danych.

Biblioteka socket Pythona zawiera narzędzia umożliwiające konwersję kolejności bajtów sieci(network byte order)
na kolejność bajtów hosta(host byte order) i odwrotnie. Są to odpowiednio funkcje ntohl()/htonl()
"""
def convert_integer():
    data = 1234
    # 32-bit
    print(f"Original: {data} => Long host byte order: {socket.ntohl(data)}, Network byte order: {socket.htonl(data)}")
    # 16-bit
    print(f"Original: {data} => Short host byte order: {socket.ntohs(data)}, Network byte order: {socket.htons(data)}")     

"""
w tym skryptlecie konwertujemy liczbę całkowitą  pomiędzy network i host byte order. Funkcja klasy socket ntohl()
konwertuje kolejność bajtów sieci na kolejność bajtów hosta w długim formacie. Tutaj n oznacza sieć, a h oznacza
host; l oznacza długi format a s krótki (16-bitowy).
"""
def main(args):
    convert_integer()
    


if __name__=="__main__":
    import sys
    import socket
    sys.exit(main(sys.argv)) 