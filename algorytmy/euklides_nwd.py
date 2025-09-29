def nwd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def NWD(a, b):
    if a != b:
        if a > b:
            return NWD(a - b, b)
        else:
            return NWD(a, b - a)
    return a



print(NWD(12,18))
