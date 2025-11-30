"""
Czasami trzeba przetłumaczyć nazwę hosta komputera na odpowiadający mu adres IP, 
na przykład w celu szybkiego wyszukania nazwy domeny. W tym przepisie przedstawiono 
prostą funkcję, która może to zrobić.

Funkcja get_remote_machine jest wraperem dla metody gethostbyname().
Dodatkowo wprowadzona została obsługa wyjatków. Oznacza to, że jeśli podczas wykonywania tej 
funkcji wystąpi jakiś błąd, zostanie on przechwycony przez  blok try-except.
"""

def get_remote_machine_info():
    remote_host =input ("remote host name: ")
    try:
        print("Adres IP hosta %s: %s" %(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print (f"{remote_host}: {err_msg}")

def main(args):
    get_remote_machine_info()
    


if __name__=="__main__":
    import sys
    import socket
    sys.exit(main(sys.argv)) 