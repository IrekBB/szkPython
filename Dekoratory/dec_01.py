import sys

def greet(name):
    return f"Hello, {name}!"

def hello(func):
    name = input("Pdaj imię: ")
    return func(name)

def respect(maybe):
    def congrats():
        return "Congrats, bro!"
    def insult():
        return "You're silly!"
    if maybe == "yes":
        return congrats()
    else:
        return insult()


def main(args):
    print ("---   Funkcja która zwraca funkcję  ---")
    print(hello(greet))
    print ("Funkcje zdefiniowane wewnatrz " \
    " funkcji")
    print (respect("yes"))
    print (respect("no"))



if __name__ =="__main__":
    sys.exit(main(sys.argv))