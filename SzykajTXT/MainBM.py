def main(args):
    t = " Z pamiętnika młodej lekarki"
    print(t)
    print("012345678901234567890123456789")
    print(f"Wynik/pozycja poszukiwań słowa 'lek' = {s.bm('lek', t)}")
    print(f"Wynik/pozycja poszukiwań słowa 'pa' = {s.bm('pa', t)}")
    print(f"Wynik/pozycja poszukiwań słowa 'parapet' = {s.bm('parapet', t)}")
    print(f"Wynik/pozycja poszukiwań słowa 'młodej' = {s.bm('młodej', t)}")
    print(f"Wynik/pozycja poszukiwań słowa 'koperta' = {s.bm('koperta', t)}")
    
if __name__=="__main__":
    import sys
    from MojeTypy import szukaj as s
    sys.exit(main(sys.argv))