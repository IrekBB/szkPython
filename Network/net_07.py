"""
Handling socket errors
W aplikacjach sieciowych częstym jest, że przy próbie połączenia jedna ze stron nie odpowiada 
np. z powodu awarii nośnika sieciowego. Biblioteka gniazd Pythona oferuje elegancką metodę
przechwytywania  takich  błędów (thesocket.error).

W celu uzyskania danych wejściowych użytkownika, został wykorzystany moduł argparse.
Moduł ten ma większe możliwości niż sys.argv. W blokach try-except należy umieścić typowe operacje 
wykonywane na gniazdach (tworzenie obiektu gniazda, łączenie z serwerem, wysyłanie danych itp.)

"""

def main():
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
    # Second try-except block -- connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)
    # Third try-except block -- sending data
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)
    while 1:
        # Fourth tr-exception block -- waiting to receive
        # data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf.decode('utf-8'))

"""
W powyższym przykładzie użyto czterech bloków try-except. 
Wszystkie bloki używają socket.error z wyjątkiem drugiego bloku,
który wykorzystuje secket.gaierror. Wyjatek secket.gaierror pojawia się 
w przypadku błędów związanych z adresem. Oprócz wymienionych wyjątków 
istnieją dwa inne typy — socket.herror, używany w przypadku starszego
interfejsu API w języku C oraz  socket.timeout - który pojawia się podczas
użycia metody settimeout() gniazda, gdy w gnieździe tym nastąpi przekroczenie 
limitu czasu połączenia.
"""    


if __name__=="__main__":
    import sys
    import socket
    import argparse
    sys.exit(main()) 