"""
Jednym z klasycznych już chyba przykładów na dekoratory jest cache. 
Utworzymy dekorator o nazwie cache dla funkcji get_web_page zwracającej dane z serwisu internetowego:


Python dostarcza kilka wbudowanych dekoratorów, które są często używane:


@staticmethod - przekształca metodę klasy w metodę statyczną, która nie przyjmuje argumentu self. Metody statyczne są używane, 
gdy funkcjonalność metody nie zależy od instancji klasy i może być wywoływana bez tworzenia obiektu klasy.


@classmethod - przekształca metodę klasy w metodę klasową, która przyjmuje argument cls (odwołanie do klasy) zamiast self. 
Metody klasowe są używane, gdy funkcjonalność metody dotyczy klasy jako całości, a nie konkretnej instancji.


@property - przekształca metodę w atrybut, co pozwala na dostęp do metody bez użycia nawiasów. 
Jest to przydatne do enkapsulacji danych i kontrolowania dostępu do atrybutów klasy. 
Dzięki temu można na przykład wprowadzić logikę walidacji lub przetwarzania danych podczas odczytu lub zapisu atrybutu.

"""
import sys

class WebMock():
     def get(self, url):
         return url + " always works!"
 
def cache(wrapped_function):
    def wrapper(web, url):
        if url in "https://chyla.org/":
            return "It work's!"
        else:
            return wrapped_function(web, url)
    return wrapper

@cache
def get_web_page(web, url):
    return web.get(url)

def main(args):
    web = WebMock()
    page = get_web_page(web, "chyla.org")
    print("chyla.org content: " + page)
    page = get_web_page(web, "google.com")
    print("google.com content: " + page)

if __name__ =="__main__":
    sys.exit(main(sys.argv))