def iloczyn_wektorowy(X, Y, Z):
    x1, y1 = Z[0] - X[0], Z[1] - X[1]
    x2, y2 = Y[0] - X[0], Y[1] - X[1]
    return x1 * y2 - x2 * y1

def sprawdz(X, Y, Z):
    return (min(X[0], Y[0]) <= Z[0] <= max(X[0], Y[0]) and
            min(X[1], Y[1]) <= Z[1] <= max(X[1], Y[1]))

def czy_przecinaja(A, B, C, D):
    v1 = iloczyn_wektorowy(C, D, A)
    v2 = iloczyn_wektorowy(C, D, B)
    v3 = iloczyn_wektorowy(A, B, C)
    v4 = iloczyn_wektorowy(A, B, D)

    if ((v1 > 0 > v2 or v1 < 0 < v2) and (v3 > 0 > v4 or v3 < 0 < v4)):
        return True

    if v1 == 0 and sprawdz(C, D, A):
        return True
    if v2 == 0 and sprawdz(C, D, B):
        return True
    if v3 == 0 and sprawdz(A, B, C):
        return True
    if v4 == 0 and sprawdz(A, B, D):
        return True

    return False

def main():
    A = tuple(map(int, input("Podaj wspólrzedne punktu A: ").split()))
    B = tuple(map(int, input("Podaj wspólrzedne punktu B: ").split()))
    C = tuple(map(int, input("Podaj wspólrzedne punktu C: ").split()))
    D = tuple(map(int, input("Podaj wspólrzedne punktu D: ").split()))

    if czy_przecinaja(A, B, C, D):
        print("Odcinki sie przecinaja")
    else:
        print("Odcinki sie nie przecinaja")

if __name__ == "__main__":
    main()
