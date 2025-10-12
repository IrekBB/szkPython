def main(args):
    print ("Przeszukiwany ciąg znaków")
    t = "abcd1010ef"
    print (t,"\n0123456789...")
    w = "1010"
    s.init_shifts(w)
    print(f" szukam {w} w {t}: {s.kmp(w,t)}")
    w = "kotek"
    s.init_shifts(w)
    print(f" szukam {w} w {t}: {s.kmp(w,t)}")

if __name__=="__main__":
    import sys
    from MojeTypy import szukaj as s
    sys.exit(main(sys.argv))