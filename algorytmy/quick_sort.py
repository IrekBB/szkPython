def quicksort(t):
    # jeżeli tablica jest pusta lub ma jeden element, to nie trzeba nic robić, można ją zwrócić.
    if len(t) <= 1:
        return t

    # wybierasz pivot (tutaj na końcu)
    pivot = t[-1]
    smaller = []
    greater = []

    # wszystkie mniejsze lub równe wartości od pivota idą do listy smaller a większe do greater.
    # len(t) - 1, bo pracujemy na elementach bez ostatniego, którym jest pivot.
    for i in range(0, len(t) - 1):
        if t[i] <= pivot:
            smaller.append(t[i])
        else:
            greater.append(t[i])

    # zwracasz tablicę, gdzie wszystkie mniejsze wartości są po lewej, a większe po prawej od pivota,
    # a pivot trafia na miejsce końcowe w tablicy wyjściowej.
    return quicksort(smaller) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    arr = [60, 20, 11, 122, 214, 345, 1324, 1, 2, 3, 6, 74, 3, 9]
    print(quicksort(arr))
