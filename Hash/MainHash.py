def main(args):
    s = "Ala ma kota"
    lst = [1, 2, 3, "Aaaa", 'Z']
    print (hash(s))   # Wbudowana hashująca funkcja pythona, wykorzystana  do  konstrukcji słowników (typ dict)
    # print (hash(lst))   # TypeError: unhashable type: 'list', bo lista jest modyfikowalna

    o1 = H.Element(35, "Kowalski")
    o2 = H.Element(35, "Kowalski")
    o3 = H.Element(32, "Kowalska")
    print ("Prywatna funkcja hash(), obiekt o1: ", hash(o1))
    print ("A co z funkcją H1 (obiekt o1)? ", H.H1(str(o1)))
    print ("Prywatna funkcja hash(), obiekt o2: ", hash(o2))
    print ("Prywatna funkcja hash(), obiekt o3: ", hash(o3))
    print (o1==o2)

if __name__ == "__main__":
    from MojeTypy import Hash as H
    import sys
    sys.exit(main(sys.argv)) 