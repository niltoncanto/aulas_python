'''
Mergesort
Mergesort é outro algoritmo de ordenação baseado no princípio da divisão e conquista. 
Ele divide o array em duas metades, ordena cada uma delas e depois mescla as duas partes ordenadas.

Passos do Mergesort:

1 Dividir o array em duas metades.
2 Ordenar cada metade recursivamente.
3 Mesclar as duas metades ordenadas.
Exemplo em Python:
'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

merge_sort([70,10,80,20,60])