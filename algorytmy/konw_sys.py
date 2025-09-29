def konwersja_z_dec (n,p):
    L=[]
    if n==0:
        return 0
    while n>0:
        r =  n%p
        if   r==10:   L.append('A')
        elif r==11:   L.append('B')
        elif r==12:   L.append('C')
        elif r==13:   L.append('D')
        elif r==14:   L.append('E')
        elif r==15:   L.append('F')
        else:
            L.append(r)
        n=n//p
    bin=''
    for i in L[::-1]:
        if isinstance(i, str): bin=bin + i
        else:
         bin=bin + str(i)
    return bin

def konwersja_na_dec(n,p):
    if p in (2,3,4,5,6,7,8,9,10):
        liczba=0
        q=0
        while n!=0:
            r = n%10
            liczba= liczba + pow(p,q) * r
            n=n//10
            q=q+1 
        return liczba
    else:
        liczba=0
        q=0
        for i in n[::-1]:
           if i in ('a','A'):
               liczba = liczba + 10 * pow(p,q)
           elif i in ('b','B'):
               liczba = liczba + 11 * pow(p,q)
           elif i in ('c','C'):
               liczba = liczba + 12 * pow(p,q)
           elif i in ('d','D'):
               liczba = liczba + 13 * pow(p,q)
           elif i in ('e','E'):
               liczba = liczba + 14 * pow(p,q)
           elif i in ('f','F'):
               liczba = liczba + 15 * pow(p,q)
           else:
               liczba = liczba + int(i) * pow(p,q)
           q=q+1       
    return liczba

slownikH = {
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
    '9':'1001',
    '8':'1000',
    '7':'0111',
    '6':'0110',
    '5':'0101',
    '4':'0100',
    '3':'0011',
    '2':'0010',
    '1':'0001',
    '0':'0000',
}

    

def hex_na_bin(n):
    n=n.upper()
    liczba=''
    for i in n[::-1]:
        for klucz in slownikH:
            if i == klucz:
                liczba = slownikH[klucz] + liczba
    return liczba

slownikOCT={
    '7':'111',
    '6':'110',
    '5':'101',
    '4':'100',
    '3':'011',
    '2':'010',
    '1':'001',
    '0':'000',
}

def oct_na_bin(n):
    liczba=''
    for i in n[::-1]:
        for klucz in slownikH:
            if i == klucz:
                liczba = slownikOCT[klucz] + liczba
    return liczba

print (oct_na_bin('17'))
   

    
        
            
            
