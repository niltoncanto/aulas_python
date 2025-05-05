def bubble_sort(arr):
    n = len(arr)
    for j in range(n):
        trocado = False
        for i in range(0, n-j-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                trocado = True
        if trocado==False:
            break
    return arr

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Lista Ordenada:", arr)
