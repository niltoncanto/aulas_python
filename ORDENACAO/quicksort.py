'''
Quicksort
Quicksort é um algoritmo de ordenação eficiente que utiliza uma abordagem de divisão e conquista. 
O algoritmo escolhe um "pivô" e particiona o array de modo que todos os elementos menores que o pivô fiquem à esquerda e todos os maiores à direita. Em seguida, aplica o mesmo processo nas duas subpartes.

Passos do Quicksort:

1 Escolher um elemento do array como pivô.
2 Reorganizar os elementos do array, de modo que todos os que são menores 
que o pivô venham antes dele e todos os maiores venham depois.
3 Recursivamente aplicar os passos anteriores aos sub-arrays de elementos menores e maiores.
Exemplo em Python:
'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [50,30,10,40,20]
print(quicksort(arr))



def quicksort1(arr, low, high):
    if low < high:
        # Função de partição que escolhe um pivô e coloca todos os menores à esquerda
        # e todos os maiores à direita do pivô
        pi = partition(arr, low, high)

        # Chama recursivamente quicksort nas duas metades
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # escolhe o último elemento como pivô
    i = low - 1

    for j in range(low, high):
        # Se o elemento atual é menor ou igual ao pivô
        if arr[j] <= pivot:
            i += 1  # incrementa o índice do menor elemento
            arr[i], arr[j] = arr[j], arr[i]  # troca

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Exemplo de uso
arr = [10, 7, 8, 9, 1, 5]
quicksort1(arr, 0, len(arr) - 1)
print(arr)
