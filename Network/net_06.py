"""
Setting and getting the default socket timeout

Czasami trzeba zmienić domyślne wartości niektórych właściwości biblioteki socket,
na przykład limit czasu  łączenia.

Tworzymy instancję obiektu klasy socket, nastepnie wywołujemy metodę gettimeout()
w celu uzyskania domyślnej wartości limitu czasu gniazda. Zmieniamy go za pomocą
metody settimeout().
"""

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print (f"Domyslny limit czasu oczekiwania gniazda(timeout):{s.gettimeout()}")
    s.settimeout(100)
    print(f"Aktualny limit czasu oczekiwania gniazda(timeout): {s.gettimeout()}")
    
"""
W tym fragmencie kodu najpierw utworzyliśmy obiekt gniazda s, przekazując rodzinę gniazd i typ gniazda
jako pierwszy i drugi argument konstruktora gniazda. Następnie uzyskalismy wartość limitu czasu
oczekiwania gniazda na którym zostanie podjęta próba połączenia - wywołując funkcję gettimeout() i zmieniając jej
​​wartość, poprzez wywołanie metody settimeout(). Wartość limitu czasu przekazywana do metody settimeout()
może wynosić kilka sekund (liczba zmiennoprzecinkowa nieujemna) lub brak argumentu. Jest to przykład metody służącej
do manipulowania operacjami blokujacymi gnizado. Ustawienie limitu czasu bez argumentu powoduje wyłączenie
limitu czasu operacji łaczenia gniazda.
"""

if __name__=="__main__":
    import sys
    import socket
    sys.exit(test_socket_timeout()) 