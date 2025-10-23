import sys

# Powszechną praktyką jest umieszczanie inna_funkcja w funkcji dekoratora 
# i wywołanie w niej pierwotnego obiektu (w omawianym przypadku jest to funkcja)

def dekorator(obj):
    def inna_funkcja():
        obj()
        print("world")
    return inna_funkcja

@dekorator
def funkcja():
    print("hello")


def main(args):
    funkcja()

if __name__ =="__main__":
    sys.exit(main(sys.argv))