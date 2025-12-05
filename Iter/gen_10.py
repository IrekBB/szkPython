"""
2. Throw .metod
Metoda .throw() umożliwia zgłoszenie wyjątku wewnątrz generatora, co może być pomocne 
przy obsłudze błędów lub sygnalizowaniu określonych warunków.
"""

def resilient_generator():
    try:
        for i in range(5):
            yield i
    except ValueError:
        yield "Error occurred!"


def main(args):
    # Using the generator
    gen = resilient_generator()
    print(next(gen))  # Output: 0
    print(next(gen))  # Output: 1
    print(gen.throw(ValueError))  # Output: "Error occurred!"

"""
Oto jak to działa: 
Generator funkcjonuje do momentu wywołania metody .throw().   
Wówczas zgłaszany jest wyjatek wewnątrz generatora, który może zostać  przechwycony i obsłuzony za pomocą bloku try-except.
"""

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))