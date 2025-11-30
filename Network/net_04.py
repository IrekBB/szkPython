"""
Finding a service name, given the port and protocol

Jeśli chcesz sprawdzić, jakie usługi sieciowe działają na hoście, przeanalizuj 
jego otwarte porty, korzystając z protokołu TCP lub UDP.

Jeśli znasz numer portu usługi sieciowej, możesz znaleźć nazwę zwiazanej z nim usługi za pomocą funkcji klasy socket 
getservbyport(). Opcjonalnie możesz podać nazwę protokołu podczas wywoływania tej funkcji.
"""
def find_service_name():
    protocolname = 'tcp'
    for port in [80,25]:
        print (f"Port:{port} => service name: {socket.getservbyport(port,protocolname)}")
    print(f"Port:53 => service name: {socket.getservbyport(53,'udp')}")

def main(args):
    find_service_name()
    


if __name__=="__main__":
    import sys
    import socket
    sys.exit(main(sys.argv)) 