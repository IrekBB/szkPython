""""
Modifying a socket's send/receive buffer sizes
W wielu sytuacjach okazuje się, że bufor gniazda ma nieodpowiednie rozmiary.
Wówczas możemy zmienić jego wartość domyślną na taką jaka nam odpowiada.

Naprzód definiujemy dwie stałe: SEND_BUF_SIZE/RECV_BUF_SIZE, 
następnie opakujemy instację gniazda  metodą setsockopt().
Dobrą praktyka jest także sprawdzenie wartości rozmiaru bufora przed jego modyfikacją.
Pamiętaj, że  osobno ustawiamy rozmiar bufora wysyłania i odbierania.

"""
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print ("Buffer size [Before]:%d" % bufsize)
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE)
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print ("Buffer size [After]:%d" %bufsize)
"""
Wywołujemy metody getsockopt() i setsockopt() na obiekcie gniazda, aby odpowiednio 
pobrać i zmodyfikować właściwości obiektu gniazda. Metoda setsockopt() przyjmuje trzy argumenty: 
level, optname i value. optname przyjmuje wartość odpowiadajacą nazwie opcji, value - jest jej  
wartością. Dla pierwszego argumentu potrzebne stałe symboliczne można znaleźć w module gniazda (SO_*etc.).

setsockopt() options are organized in groups identified by levels. 
There are socket-level options, IP-level options, TCP-level options,
etc. SO_REUSEADDR (and SO_REUSEPORT) is a socket-level option, as it
affects the socket object itself (when it is binding to a local IP/port pair)
"""

def main(args):
    modify_buff_size()

if __name__=="__main__":
    import sys
    import socket
    sys.exit(main(sys.argv)) 