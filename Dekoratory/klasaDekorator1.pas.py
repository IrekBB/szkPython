<<<<<<< HEAD
import sys
class Spam:
    numInstances = 0   # zmienna klasy! Nie obiektu - zmienna statyczna
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1  # Każde utworzenie obieku powoduje jej inkrementację
    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)


def main(args):
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstances()

if __name__ == "__main__":
=======
import sys
class Spam:
    numInstances = 0   # zmienna klasy! Nie obiektu - zmienna statyczna
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1  # Każde utworzenie obieku powoduje jej inkrementację
    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)


def main(args):
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstances()

if __name__ == "__main__":
>>>>>>> 04a243ce5a1b07f507b75f71b1dcf09ce156c7db
    sys.exit(main(sys.argv))