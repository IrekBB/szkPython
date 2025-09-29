def merge_sort(tab):
    if len(tab) < 2:
        return tab
	
    i = j = k = 0
    mid = len(tab) // 2
    L, R = tab[:mid], tab[mid:]
    merge_sort(L)
    merge_sort(R)

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            tab[k] = L[i]
            i += 1
        else:
            tab[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        tab[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        tab[k] = R[j]
        j += 1
        k += 1

L=[23, 47, 81, 95, 7,14,39,55,62,74]
merge_sort(L)
print(L)
