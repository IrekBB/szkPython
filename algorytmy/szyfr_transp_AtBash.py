"""
Jest to monoalfabetyczny szyfr podstawieniowy, ograniczony.
Zasada jego działania polega na podstawieniu zamiast danej litery,
litery leżącej po drugiej stronie alfabetu w takiej samej odległości.
Np. zamiast litery A powinniśmy podstawić literę Z,
za literę C wstawiamy literę X.
"""
def atbash_kod(txt):
    txt = list(txt)
    for i in range(len(txt)):
        if "A" <= txt[i] <= "Z":  # wielkie litery
            txt[i] = chr(ord("Z") - (ord(txt[i]) - ord("A")))

        if "a" <= txt[i] <= "z":  # małe litery
            txt[i] = chr(ord("z") - (ord(txt[i]) - ord("a")))

        if txt[i] == " ":
            txt[i] = " "

    return "".join(txt)

def atbash_dekod(txt):
    txt = list(txt)
    for i in range(len(txt)):
        if "A" <= txt[i] <= "Z":  # wielkie litery
            txt[i] = chr(ord("A") + (ord("Z")-ord(txt[i])))

        if "a" <= txt[i] <= "z":  # małe litery
            txt[i] = chr(ord("a") + (ord("z")-ord(txt[i])))

        if txt[i] == " ":
            txt[i] = " "

    return "".join(txt)


def main(args):
    txt = "SzyfrPrzestawieniowyAtbash"
    kod = atbash_kod(txt)
    print(kod)
    print(atbash_dekod(kod))
    
    

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
    
