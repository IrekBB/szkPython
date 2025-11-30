"""
Iterator to nic innego jak kontener, który implementuje protokół iteracji. Opiera się na dwóch metodach:
• __next__: zwraca kolejny obiekt kontenera
• __iter__: zwraca sam iterator """

def main(args):
    i = iter('abc')
    while True:
        try:
            print(next(i))
        except StopIteration:
            print ("Nie ma co dalej iterować!")
            break
    print("koniec...")
    


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv)) 