"""
Converting an IPv4 address to different formats

W przypadku funkcji sieciowych niskiego poziomu, zdarza się, że zwykła notacja adresów IP nie jest zbyt przydatna.
Muszą one zostać przekonwertowane na spakowane 32-bitowe formaty binarne.

Biblioteka gniazd Pythona zawiera narzędzia do obsługi różnych formatów adresów IP. Tutaj użyjemy dwóch z nich: 
inet_aton() i inet_ntoa(). Utworzymy funkcję convert_ip4_address(), gzie za pomocą funkcji inet_aton() i inet_ntoa() 
spakujemy i rozpakujemy odpowiednio dwa przykładowe adresy IP, 127.0.0.1 i 192.168.0.1.


"""
def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print ("IP Address: %s => Packed: %s, Unpacked: %s" %(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

"""
W tym skryptlecie dwa adresy IP zostały przekonwertowane z ciągu znaków na 32-bitowy format spakowany przy użyciu instrukcji for-in.
Dodatkowo z modułu binascii wywoływana jest funkcja hexlify języka Python, która pozwala na reprezentowanie danych binarnych 
w formacie szesnastkowym.
"""

def main(args):
    convert_ip4_address()
    


if __name__=="__main__":
    import sys
    import socket
    from binascii import hexlify
    sys.exit(main(sys.argv)) 