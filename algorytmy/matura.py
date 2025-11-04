def przestaw(n : int) -> int:
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    if n > 0:
        w = a + b*10 + przestaw(n)*100
    else:
        if a > 0:
            w = a+10*b
        else:
            w = b
    return w


def przestaw2(n : int) -> int:
    w = 0
    m = 1

    while n > 0:
        r = n % 100
        a = r // 10
        b = r % 10

        if a > 0:
            w += (10*b + a) * m
        else:
            w += b*m
        
        n//=100
        m*=100
    return w

print(przestaw(43657688))
print(przestaw(154005710))
print(przestaw(998877665544321))
print(przestaw(316498))

print(przestaw2(43657688))
print(przestaw2(154005710))
print(przestaw2(998877665544321))
print(przestaw2(316498))
i = input("WAITING...")
