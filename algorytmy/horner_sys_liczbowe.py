def horner(s,p):
    L=int(s[0])
    for i in range(1,len(s)):
        L=L*p + int(s[i])
    return L


print (horner('1111',2))
